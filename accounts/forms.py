from django.contrib.auth.forms import UserCreationForm
from .models import Accounts

class AccountsCreationForm(UserCreationForm):
    class Meta:
        model = Accounts
        fields = ['username', 'email', '', '']