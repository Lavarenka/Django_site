from django.shortcuts import render, get_object_or_404, redirect

from .models import News, Category
from .forms import NewsForm


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

# функция открытия конкретной записи, c фильтром на ошибку 404
# если есть 404 то поисковик исключает из индекса
def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})

def add_news(request):
    if request.method == 'POST': # POST отправление данных из формы
        form = NewsForm(request.POST) # принять данные с формы
        if form.is_valid():
            # news = News.objects.create(**form.cleaned_data)# обработчик данных
            news = form.save()
            return redirect(news) # после отправки формы закидывает по ссылке
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
