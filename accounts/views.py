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