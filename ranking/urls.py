# coding:utf-8

from django.urls import path
from ranking.views import show_ranking

urlpatterns = [
    path('show_ranking/', show_ranking, name='show_ranking'),
]
