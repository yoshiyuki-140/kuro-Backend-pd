from typing import Any
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView
from topics.models import Topics

# Create your views here.


class ToppageView(TemplateView):
    template_name = 'general/top.html'
    topic = get_object_or_404(Topics)
    
    # コンテキストに何を入れるのかを追加で指定する
    # get_context_dataのオーバーライドをしているので
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["topics"] = get_object_or_404(Topics)
        return context
    
