from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


# viewで指定するテンプレートにコンテキストを渡す場合は下のように変更するとよい
# class TopPageView(TemplateView):
#     template_name = "top.html"
#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context["message"] = "Template viewの変数"
#         return super().get_context_data(**kwargs)
