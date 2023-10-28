from typing import Any
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView
from topics.models import Topic

# Create your views here.


class ToppageView(TemplateView):
    template_name = 'general/top.html'
    # ここでget_object_or_404を使用してTopicsのテーブルオブジェクトを指定するとtopicのデータテーブルを参照してしまいマイグレーション前に 
    # "such table not found" エラーが出る
    
    # コンテキストに何を入れるのかを追加で指定する
    # get_context_dataのオーバーライドをしているので
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        self.topic = Topic.objects.all()
        context["topics"] = self.topic
        return context
    
