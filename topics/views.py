from django.shortcuts import render, redirect
from topics.models import *
from django.http import HttpResponse
from django.utils.html import escape

# Create your views here.
UserModel = get_user_model()


def detail_topic(request, topic_id):
    '''
    投稿表示画面
    '''
    template_name = 'topics/detail_topic.html'
    topic = Topic.objects.get(pk=topic_id)

    return render(request, template_name, context={'topic': topic})


def create_comment(request, topic_id):
    '''
    投稿表示画面(コメント投稿)
    '''
    template_name = 'topics/create_comment.html'
    return render(request, template_name)


def create_topic(request):
    '''
    投稿画面
    '''
    # tepmalteの場所を定義
    template_name = 'topics/create_topic.html'

    if request.method == "POST": # 押されたボタンに関わらずPOSTされた時に実行
        if "button_submit_topic" in request.POST: # 投稿ボタンが押された時の処理
            '''
            ここはバリデーションやサニタイズが必要
            '''
            # リクエストから入力データを取得
            title = request.POST.get('title')
            description = request.POST.get('description')

            # バリデーション : タイトルと説明が空でないことを確認
            if not title or (not description):
                return HttpResponse("タイトルと説明は必須です.")

            # サニタイズ
            title = escape(title)
            description = escape(description)

            # モデルインスタンスの生成
            topic = Topic.objects.create(
                title=title,
                description=description, 
                created_by = UserModel.objects.get(pk=1) # ここは変更しないといけないpk=
                # 変えるならしたみたいな感じ
                # created_by = request.user
            )

            # データベースに保存
            topic.save()

            # 成功時はcomplate_create_topicへリダイレクト
            return redirect('complate_create_topic')

        # 成功時はcomplate_create_topicへリダイレクト
        return redirect('compelte_create_topic')

    # POST等が場合は以下を実行して、template_nameをレンダリング
    return render(request, template_name)


def complete_create_topic(request):
    '''
    投稿完了画面
    '''
    template_name = 'topics/complete_create_topic.html'
    return render(request, template_name)
