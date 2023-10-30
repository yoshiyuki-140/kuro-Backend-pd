from django.shortcuts import render
from topics.models import Topic, Comment, Tag

# Create your views here.


def top(request):
    template_name = 'general/top.html'
    topics = Topic.objects.all()
    context = {
        'topics': topics
    }
    return render(request, template_name, context)
