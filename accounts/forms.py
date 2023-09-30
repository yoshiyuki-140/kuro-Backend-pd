from django.contrib.auth.forms import UserCreationForm
from .models import Accounts

class AccountsCreationForm(UserCreationForm):
    '''
    UserCreationFormのサブクラス
    '''
    class Meta:
        model = Accounts
        # fields = ('name', 'birth_data', 'email', 'password','region','profession')
        fields = ('username', 'email', 'password1', 'password2')