from django.urls import path
# viewsモジュールをインポート
from . import views

from django.contrib.auth import views as auth_views


# パターン逆引きのための名付け
app_name = "accounts"

urlpatterns = [
    # サインアップビューの呼び出し
    path(
        'signup/',
        views.SignUpView.as_view(),
        name='signup',
    ),
    path(
        'signup_success/',
        views.SignUpSuccessView.as_view(),
        name='signup_success'
    ),

    # こっからはカスタマイズしてないDjango既存ライブラリをぶん回す
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='acccounts/login.html'),
        name='login',
    ),
    # 「http(s)://<ホスト名>/logout/」へのアクセスに対して、ログアウトを実行させる
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='accounts/logout.html'),
        name='logout',
    )
]
