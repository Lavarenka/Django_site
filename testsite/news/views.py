from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import News, Category
from .forms import NewsForm

class HomeNews(ListView):
    model = News # получаем данные из таблицы новостей
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self): # фильтр, показывает только публикованные
        return News.objects.filter(is_published=True)

class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False #если список категории пустой то не показываем

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self): # фильтр, показывает только публикованные
        return News.objects.filter(category_id=self.kwargs['category_id'] ,is_published=True)


class ViewNews(DetailView):
    model = News
    template_name = 'news/view_news.html'
    # pk_url_kwarg = 'news_id'
    context_object_name = 'news_item'

class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home') # после добавления новости переводит на главную


# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     # 1 параметр request, 2 параметр название шаблона, 3 параметр контекст
#     return render(request, 'news/index.html', context)

# def get_category(request, category_id):
#     news = News.objects.filter(category_id = category_id) # фильтр для выборки определнных категорий
#     category = Category.objects.get(pk=category_id) # вытягиваем с бд категории
#     context = {
#         'news' : news,
#         'category': category
#     }
#     return render(request, 'news/category.html',context )
# возврощает страничку с данными

# функция открытия конкретной записи, c фильтром на ошибку 404
# если есть 404 то поисковик исключает из индекса
# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {"news_item": news_item})

# def add_news(request):
#     if request.method == 'POST': # POST отправление данных из формы
#         form = NewsForm(request.POST) # принять данные с формы
#         if form.is_valid():
#             # news = News.objects.create(**form.cleaned_data)# обработчик данных
#             news = form.save()
#             return redirect(news) # после отправки формы закидывает по ссылке
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
