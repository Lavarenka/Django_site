from django.shortcuts import render
from django.http import HttpResponse

from .models import News


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    # 1 параметр request, 2 параметр название шаблона, 3 параметр контекст
    return render(request, 'news/index.html', context)

