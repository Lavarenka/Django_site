from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories,
    }
    # 1 параметр request, 2 параметр название шаблона, 3 параметр контекст
    return render(request, 'news/index.html', context)

def get_category(request, category_id):
    news = News.objects.filter(category_id)