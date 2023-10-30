from django.shortcuts import render

# Create your views here.


def detail_topic(request, topic_id):
    '''
    投稿表示画面
    '''
    template_name = 'topics/detail_topic.html'
    return render(request, template_name)


def create_comment(request,topic_id):
    '''
    投稿表示画面(コメント投稿)
    '''
    template_name = 'topics/create_comment.html'
    return render(request, template_name)


def create_topic(request):
    '''
    投稿画面
    '''
    template_name = 'topics/create_topic.html'
    return render(request, template_name)


def complete_create_topic(request):
    '''
    投稿完了画面
    '''
    template_name = 'topics/complete_create_topic.html'
    return render(request, template_name)
