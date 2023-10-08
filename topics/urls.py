from django.urls import path
from views import topic_new,topic_edit,topic_detail

app_name = "topics"

urlpatterns = [
    path('topic_new/',topic_new,name='topic_new'),
    path('topic_edit/',topic_edit,name='topic_edit'),
    path('topic_detail/',topic_detail,name='topic_detail'),
]
