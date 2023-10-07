from django.forms import ModelForm
from topics.models import Topics,Comments


class TopicForm(ModelForm):
    class Meta:
        model = Topics
        fields = ('title','description')

        
class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('comments')
