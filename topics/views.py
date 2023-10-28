from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden,HttpResponseRedirect
from .forms import TopicForm,CommentForm
# from django.views.generic import *
from django.contrib import messages
from django.shortcuts import resolve_url
from .models import Topic,Comment


# topic views 
def topic_new(request):
    template_name = 'topics/topic_new.html'
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.created_by = request.user
            topic.save()
            successMsg = "課題を投稿しました"
            messages.success(request,successMsg)
            return redirect(topic_detail,topic_id=topic.pk)
        else:
            messages.error(request,"Form's contents is not correct.")
    else:
        form = TopicForm()

    return render(request,template_name,{'form':form})

def topic_detail(request,topic_id):
    template_name = 'topics/topic_detail.html'
    # topic = Topic.objects.get(pk=topic_id)
    topic = get_object_or_404(Topic,pk=topic_id)
    comments = Comment.objects.filter(topic=topic)
    context = {
        'topic':topic,
        'comments':comments
        }
    return render(request,template_name,context)

def topic_edit(request,topic_id):
    '''
    課題編集用のtopic
    '''
    template_name = 'topics/topic_edit.html'
    topic = get_object_or_404(Topic,pk=topic_id)
    # if topic.created_by_id != request.user.id:
    if topic.created_by != request.user.id:
        errorMsg = "この話題の編集は許可されていません"
        return HttpResponseForbidden(errorMsg)
        
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid(): # この分岐いらないかもねformに投稿すれば自然に反映される鴨
            successMsg = "課題が編集されました"
            messages.success(request,successMsg)
            form.save()
            return redirect('topics/topic_detail.html',topic_id=topic_id)
    else:
        form = TopicForm(instance=topic)

    return render(request,template_name,context={'topic':form})

def topic_delete(request,topic_id):
    '''
    削除確認画面
    '''
    template_name = 'topics/topic_delete.html'
    topic = get_object_or_404(Topic,pk=topic_id)
    if topic.created_by != request.user.id:
        errorMsg = "あなたにはdelete権限がありません"
        return HttpResponseForbidden(errorMsg)

    if request.method == 'POST': # deleteボタンが押されたら
        topic.delete() # その話題をDBから削除
        messages.success(request,"課題の削除に成功しました") # 実行メッセージ
        return redirect('topics/topic_detail.html',topic_id=topic_id)
    return render(request,template_name)


# comments views

@login_required
def comment_new(request, pk:int):
    topic = get_object_or_404(Topic, pk=pk)

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
    return redirect('topics', topic_id=pk)
