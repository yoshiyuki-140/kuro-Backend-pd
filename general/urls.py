from django.urls import path
from general.views import *

urlpatterns = [
    path('home/',home,name='home'),
]
