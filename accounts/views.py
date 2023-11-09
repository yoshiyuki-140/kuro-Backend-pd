from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import BaseModelForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

# Create your views here.


def signup_success(request):
    # 会員登録成功画面
    '''アカウント
    '''
    template_name = 'accounts/signup_success.html'
    return render(request, template_name)


class SignupView(CreateView):
    app_name = "accounts"
    form_class = UserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form: BaseModelForm):
        user = form.save()
        login(self.request, user)
        messages.add_message(self.request, messages.SUCCESS, "ユーザー登録しました。")
        self.object = user
        # return HttpResponseRedirect(self.get_success_url())
        return render(request=self.request, template_name='accounts/signup_success.html')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "ユーザー登録に失敗しました。")
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    # ログアウト後のリダイレクト先を指定するためのget_success_urlメソッドをオーバーライドします。
    def get_success_url(self):
        # ログアウト後にリダイレクトしたいURLを指定します。
        return reverse_lazy('home')  # このURLをカスタマイズしてください


def profile_view(request):
    '''profile
    '''
    if request.method == "POST":
        '''編集ボタンが押されたら
        '''
        return redirect('')

    return render(request, 'accounts/profile.html', {'user': request.user})
