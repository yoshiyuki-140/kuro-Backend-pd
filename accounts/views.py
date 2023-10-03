<<<<<<< HEAD
from .forms import AccountsCreationForm
from django.views.generic import CreateView,TemplateView
from django.urls import reverse_lazy

# Create your views here.

# def nippoCreateView(request):
    # template_name = "accounts/sigunup.html"
# 
class SignUpView(CreateView):
    '''サインアップページのビュー
    '''
    # forms.pyで定義したフォームのクラス
    form_class = AccountsCreationForm
    # レンダリングするテンプレート
    template_name = "accounts/signup.html"
    # サインアップ完了後のリダイレクト先のURLパターン
    success_url = reverse_lazy('accounts:signup_success')
    
    def form_valid(self, form):
        # formオブジェクトのフィールドの値をデータベースに登録
        user = form.save()
        self.object = user
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)
 


class SignUpSuccessView(TemplateView):
    '''サインアップ成功ページのビュー
    
    '''
    # レンダリングするテンプレート
    template_name = "accounts/signup_success.html"
=======
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Create your views here.


class SignupView(CreateView):
    app_name = "accounts"
    form_class = UserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form: BaseModelForm):
        user = form.save()
        login(self.request, user)
        messages.add_message(self.request, messages.SUCCESS,"ユーザー登録しました。")

        self.object = user
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR,"ユーザー登録に失敗しました。")
        return super().form_invalid(form)


>>>>>>> master
