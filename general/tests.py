from django.test import TestCase

# Create your tests here.


class HomeTest(TestCase):
    def test_should_return_200_statuscode(self):
        '''
        home page test
        '''
        response = self.client.get('/general/home/')
        self.assertEqual(response.status_code,200)
