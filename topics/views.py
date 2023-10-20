from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden,HttpResponseRedirect
from .forms import TopicForm,CommentForm
# from django.views.generic import *
# LoginRequiredMixin：クラスベースビューをログインが確認できないと表示できないようにする継承用クラス
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DetailView,ListView
from .models import Topics,Comments

# @login_required
# def comment_new(request, pk:int):
#     topic = get_object_or_404(Topics, pk=pk)

#     form = CommentForm(request.POST)
#     if form.is_valid():
#         comment = form.save(commit=False)
#         comment.commented_to = topic
#         comment.commented_by = request.user
#         comment.save()
#         messages.add_message(request, messages.SUCCESS,
#                              "コメントを投稿しました。")
#     else:
#         messages.add_message(request, messages.ERROR,
#                              "コメントの投稿に失敗しました。")
#     return redirect('topics', topic_id=pk)

class NewCommentView(CreateView,LoginRequiredMixin):
    '''
    TopicDetailViewに移植するべき
    この構造だとORMオブジェクトが取得できない
    '''
    template_name = "topics/comment_new.html"
    model = Comments
    form_class = CommentForm
    success_url = reverse_lazy('topics:topic_detail')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        postdata = form.save(commit=False)
        postdata.commented_by = self.request.user
        postdata.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        '''
        投稿に成功した際に実行される処理を書くメソッド
        ここではメッセージを表示することをオーバーライドしている
        '''
        successMsg = "コメントを投稿しました"
        messages.success(self.request,successMsg)
        return resolve_url('top')
    

# create class base view

class NewTopicView(CreateView,LoginRequiredMixin):
    template_name = 'topics/topic_new.html'
    model = Topics
    form_class = TopicForm
    # 投稿完了のURL
    success_url = reverse_lazy('top') # generalに属していないので'general:top'ではない

    def form_valid(self, form) -> HttpResponseRedirect:
        '''
        フォームのバリデーションを通過したとき呼ばれる.
        ここでは主に投稿者を登録する
        '''
        # commit = Falseにするとpostされたデータを取得できる
        postdata = form.save(commit=False)
        # 投稿した人は誰なのかを登録
        postdata.created_by = self.request.user
        # データをデータベースに登録
        postdata.save()

        return super().form_valid(form)

       

    
    def get_success_url(self) -> str:
        '''
        投稿に成功した際に実行される処理を書くメソッド
        This method will execute, when success getting url.
        '''
        successMsg = "課題を投稿しました"
        messages.success(self.request,successMsg)
        return resolve_url('top')

class EditTopicView(UpdateView,LoginRequiredMixin):
    """
    CivicSeekにおいて課題をupdateするときに使うview要素
    """
    model = Topics
    # form_class = TopicForm
    # 表示する入力フォームの属性
    fields = ('title','description')
    # updateが完了した時のリダイレクト先の名前,
    # ここでいう「名前」とは,path関数のname属性で指定されるものと等しい意味を持つ
    success_url = reverse_lazy('topics:topic_detail')

class DetailTopicView(DetailView,LoginRequiredMixin):
    """課題の詳細を表示するページを作成するview.

    Args:
        DetailView (_type_): _description_
    """
    model = Topics
    template_name = 'topics/topic_detail.html'
    context_object_name = 'topic'

class ListTopicView(ListView):
    '''
    トップページに表示する課題の投稿内容一覧
    '''
    template_name = 'topics/topic_list.html'
    queryset = Topics.objects.all()
    # 1ページに表示するレコード数
    paginate_by = 10
