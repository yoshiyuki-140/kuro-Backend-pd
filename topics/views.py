from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .forms import TopicForm,CommentForm
from .models import Topics,Comments
from django.views.generic import *
# LoginRequiredMixin：クラスベースビューをログインが確認できないと表示できないようにする継承用クラス
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def comment_new(request, topic_id):
    topic = get_object_or_404(Topics, pk=topic_id)

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.commented_to = topic
        comment.commented_by = request.user
        comment.save()
        messages.add_message(request, messages.SUCCESS,
                             "コメントを投稿しました。")
    else:
        messages.add_message(request, messages.ERROR,
                             "コメントの投稿に失敗しました。")
    return redirect('topics', topic_id=topic_id)

# create class base view
from django.contrib import messages
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import TopicForm
from .models import Topics

class NewTopicView(CreateView,LoginRequiredMixin):
    model = Topics
    form_class = TopicForm
    # 投稿に成功した時のURL
    # ここでは実験的にトップページに飛ぶようにする
    success_url = reverse_lazy('general:top') # このコードを書いた時点ではtopはgeneralに属していないので動かない可能性が高い

    
    def get_success_url(self) -> str:
        '''
        投稿に成功した際に実行される処理を書くメソッド
        This method will execute, when success getting url.
        '''
        successMsg = "課題を投稿しました"
        messages.success(self.request,successMsg)
        return resolve_url('general:top')

class EditTopicView(UpdateView,LoginRequiredMixin):
    """
    CivicSeekにおいて課題をupdateするときに使うview要素
    """
    model = Topics
    # 表示する入力フォームの属性
    fields = ('title','description')
    # テンプレートファイルの拡張子を取り除いたものの最後につく名前ここでは"form_edit.html"を指定したいから"_edit"を指定した.
    template_name_suffix = "_edit"
    # updateが完了した時のリダイレクト先の名前,
    # ここでいう「名前」とは,path関数のname属性で指定されるものと等しい意味を持つ
    success_url = reverse_lazy('topic_detail')

class DetailTopicView(DetailView,LoginRequiredMixin):
    """課題の詳細を表示するページを作成するview.

    Args:
        DetailView (_type_): _description_
    """
    model = Topics
