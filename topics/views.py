from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from forms import TopicForm,CommentForm
from models import Topics,Comments

# Create your views here.


@login_required
def topic_new(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.created_by = request.user
            topic.save()
            messages.add_message(request, messages.SUCCESS,
                                 "トピックを作成しました。")
            return redirect(topic_detail, topic_id=topic.pk)
        else:
            messages.add_message(request, messages.ERROR,
                                 "トピックの作成に失敗しました。")
    else:

        form = TopicForm()
    return render(request, "topics/topic_detail.html", {'form': form})


@login_required
def topic_edit(request, topic_id):
    topic = get_object_or_404(Topics, pk=topic_id)
    # ここにworningを示す赤波線が出るのは
    if topic.create_by_id != request.user.id:
        return HttpResponseForbidden("このトピックの編集は許可されていません。")

    if request.method == "POST":
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "トピックを更新しました。")
            return redirect('topic_detail', topic_id=topic_id)
        else:
            messages.add_message(request, messages.ERROR,
                                 "トピックの更新に失敗しました。")
    else:
        form = TopicForm(instance=topic)
    return render(request, 'topics/topic_edit.html', {'form': form})


@login_required
def topic_detail(request, topic_id):
    topic = get_object_or_404(Topics, pk=topic_id)
    comments = Comments.objects.filter(commented_to=topic_id).all()
    comment_form = CommentForm()

    return render(request, 
        "topic_detail.html", 
        {
        'topic': topic,
        'comments': comments,
        'comment_form': comment_form,
        })

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
