from django.test import TestCase

# Create your tests here.


class Complete_create_topic_test(TestCase):
    def test_should_return_200_httpstatus_code(self):
        response = self.client.get('/topics/complete_create_topic/')
        self.assertEqual(response.status_code, 200)


class Create_comment_test(TestCase):
    def test_should_return_200_httpstatus_code(self):
        response = self.client.get('/topics/1/create_comment/')
        self.assertEqual(response.status_code, 200)


class Create_topic_test(TestCase):
    def test_should_return_200_httpstatus_code(self):
        response = self.client.get('/topics/create_topic/')
        self.assertEqual(response.status_code, 200)


class Detail_topic_test(TestCase):
    def test_should_return_200_httpstatus_code(self):
        response = self.client.get('/topics/detail_topic/1/')
        self.assertEqual(response.status_code, 200)
