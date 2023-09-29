from accounts.models import Accounts
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AccountsCreationForm

# Create your views here.
