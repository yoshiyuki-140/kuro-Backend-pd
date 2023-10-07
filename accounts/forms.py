from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

class AccountsCreationForm(UserCreationForm):
    '''
    UserCreationFormのサブクラス
    '''
    class Meta:
        model = settings.AUTH_USER_MODEL
        # fields = ('name', 'birth_data', 'email', 'password','region','profession')
        fields = ('username', 'email', 'password1', 'password2')