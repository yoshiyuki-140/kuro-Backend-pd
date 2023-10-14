from django.test import TestCase

# Create your tests here.

from django.contrib.auth import get_user_model

UserModel = get_user_model() # def setUpするときに使うかも

class TopPageViewTest(TestCase):

    def testShouldReturn200Statuscode(self):
        """'あなたの悩みを共有しましょう'という文字列がトップページに含まれているかテスト
        """
        response = self.client.get('/')
        self.assertContains(response,'あなたの悩みを共有しましょう',status_code=200)

    def testShouldUseSpecifiedTemplate(self):
        """'general/top.html'をテンプレートとして使っているかテスト
        """
        response = self.client.get('/')
        self.assertTemplateUsed(response,'general/top.html')
       