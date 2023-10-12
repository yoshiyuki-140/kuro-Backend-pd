from django.urls import path
from .views import DetailTopicView,EditTopicView,NewTopicView

# postリクエストを受け取る用のviewルーティング
from .views import comment_new

app_name = "topics"

topic_new = NewTopicView.as_view()
topic_edit = EditTopicView.as_view()
topic_detail = DetailTopicView.as_view()

urlpatterns = [
    path('topic_new/',topic_new,name='topic_new'),
    path('<int:pk>/edit',topic_edit,name='topic_edit'),
    path('<int:pk>/',topic_detail,name='topic_detail'),
    path('comment_new/',comment_new,name='comment_new'),
]
