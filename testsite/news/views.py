from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    # 1 параметр request, 2 параметр название шаблона, 3 параметр контекст
    return render(request, 'news/index.html', context)

def get_category(request, category_id):
    news = News.objects.filter(category_id = category_id) # фильтр для выборки определнных категорий
    category = Category.objects.get(pk=category_id) # вытягиваем с бд категории
    context = {
        'news' : news,
        'category': category
    }
    return render(request, 'news/category.html',context )
# возврощает страничку с данными
