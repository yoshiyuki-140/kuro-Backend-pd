from django.urls import path
from .views import DetailTopicView,EditTopicView,NewTopicView,ListTopicView

# postリクエストを受け取る用のviewルーティング
from .views import NewCommentView

app_name = "topics"

topic_new = NewTopicView.as_view()
topic_edit = EditTopicView.as_view()
topic_detail = DetailTopicView.as_view()
topic_list = ListTopicView.as_view()
comment_new = NewCommentView.as_view()

urlpatterns = [
    path('topic_new/',topic_new,name='topic_new'),
    path('<int:pk>/edit/',topic_edit,name='topic_edit'),
    path('<int:pk>/',topic_detail,name='topic_detail'),
    path('<int:pk>/comment_new/',comment_new,name='comment_new'),
    # path('topic_list/',topic_list,name='topic_list'),
]
