from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AccountsCreationForm
from django.contrib.auth import login

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = AccountsCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect()

def login(request,user_id):
    if request.method == "POST":
        form = 