from django.test import TestCase

# Create your tests here.

class SignUpTest(TestCase):
    def test_do_contain_specified_text(self):
        response = self.client.get('/accounts/signup/')
        self.assertContains(response,"会員登録",status_code=200)

    def test_is_use_template(self):
        response = self.client.get('/accounts/signup/')
        self.assertTemplateUsed(response,'accounts/signup.html')

