from django.test import TestCase

# Create your tests here.

from django.contrib.auth import get_user_model
from topics.models import Topic,Tag,Comment

UserModel = get_user_model()

class NewTopicTemplateTest(TestCase):
    def testShouldReturn200statuscodeAndContainSpecifiedString(self):
        """'課題投稿'という文字列をstatuscode200で返してきたレスポンスに含まれているかテスト
        """
        response = self.client.get('/topics/topic_new/')
        self.assertContains(response,'課題投稿',status_code=200)

    def testShouldUseSpecifiedTemplate(self):
        """指定したテンプレートを使用しているかどうかテスト
        """
        response = self.client.get('/topics/topic_new/')
        self.assertTemplateUsed(response,'topics/topic_new.html')

class EditTopicTemplateTest(TestCase):
    """'topic_new.html'を使用できるかテスト
    """

    def setUp(self):
        """テストでのみ用いるデータの作成 : テストが終わったら消される (・∀・)
        このORMコードが正しいことはデバッグ済み. -> def test(self)を作成しその中に書いた
        """
        self.user = UserModel.objects.create(
            username='test_user',
            email='test@example.com',
            password='secret',
        )

        self.tag = Tag.objects.create(
            name = 'test tag',
        )

        self.topic = Topic.objects.create(
            title = 'test topic',
            description = 'test description',
            created_by = self.user, # ここはself.user.idにしたほうがいいのかも
            # tags = self.tag.pk, # ここもself.tag.idのほうがいいかも
            like_count = 11,
        )

        self.topic.tags.add(self.tag)
        self.topic.created_by = self.user

        self.comment = Comment.objects.create(
            comment = 'test comment',
            created_by = self.user,
            commented_to = self.topic,
        )
        self.location = f'/topics/{self.user.pk}/edit/'
        self.client.force_login(self.user)

    def testShouldReturn200statuscodeAndContainSpecifiedString(self):
        """'課題編集'という文字列がstatuscode200で返してきたレスポンスに含まれているかテスト
        """
        response = self.client.get(self.location)
        self.assertContains(response,'課題編集',status_code=200)

    def testShouldUseSpecifiedTemplate(self):
        """指定したテンプレートを使用しているかどうかテスト
        """
        response = self.client.get(self.location)
        self.assertTemplateUsed(response,'topics/topics_form.html')


