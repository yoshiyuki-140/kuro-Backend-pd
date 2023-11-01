from django.urls import path
from topics.views import *

urlpatterns = [
    path('complete_create_topic/', complete_create_topic,
         name='complate_create_topic'),
    path('<int:topic_id>/create_comment/',
         create_comment, name='create_comment'),
    path('create_topic/', create_topic, name='create_topic'),
    path('detail_topic/<int:topic_id>/', detail_topic, name='detail_topic'),
]
