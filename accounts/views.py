from accounts.models import Accounts
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AccountsCreationForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = AccountsCreationForm(request.POST)
        if form.is_valid():
            accounts_data = form.save(commit=False)
            accounts_data.created_by = request.user
            # ここになんかredirect先の関数を書かないといけないとらしい.
            # return redirect()

    else:
        form = AccountsCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

@login_required
def signin(request,user_id):
    pass
