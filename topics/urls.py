from django.urls import path

# postリクエストを受け取る用のviewルーティング
from .views import *

app_name = "topics"


urlpatterns = [
    path('topic_new/',topic_new,name='topic_new'),
    path('<int:pk>/edit/',topic_edit,name='topic_edit'),
    path('<int:pk>/',topic_detail,name='topic_detail'),
    path('<int:pk>/comment_new/',comment_new,name='comment_new'),
    # path('topic_list/',topic_list,name='topic_list'),
]
