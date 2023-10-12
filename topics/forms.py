from django.forms import ModelForm
from topics.models import Topics,Comments

# ここではModelFormクラスを継承してフォームを作成しているけど
# 今後細かい設定をフォームに対して行うことがあると思うからその時は
# from django.forms import Formを実行し、Formの継承を行うこと
# Formクラスを使用したフォームの設定方法に関しては以下のURLが参考になるだろう
# https://office54.net/python/django/forms-field-argument

class TopicForm(ModelForm):
    class Meta:
        model = Topics
        fields = ('title','description')

        
class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)
