from django.urls import path
<<<<<<< HEAD
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
=======
from .views import SignupView
from django.contrib.auth.views import *

signup_view = SignupView.as_view(template_name='accounts/signup.html')
login_view = LoginView.as_view(template_name='accounts/login.html')
logout_view = LogoutView.as_view(template_name='accounts/logout.html')
password_change_view = PasswordChangeView.as_view(template_name='accounts/password_change.html')
password_change_done_view = PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html')
password_reset_view = PasswordResetView.as_view(template_name='accounts/password_reset.html')
password_reset_done_view = PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html')
password_reset_confirm_view = PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html')
password_reset_complete_view = PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html')

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', login_view, name='logout'),
    path('password_change/', password_change_view, name='password_change'),
    path('password_change/done/', password_change_done_view,name='password_change_done'),
    path('password_reset/', password_reset_view, name='password_reset'),
    path('password_reset/done/', password_reset_done_view, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', password_reset_confirm_view, name='password_reset_confirm'),
    path('reset/done/', password_reset_complete_view,name='password_reset_complete'),
]
>>>>>>> master
