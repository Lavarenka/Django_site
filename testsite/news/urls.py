from django.urls import path, include
from .views import *
# подключаем страницчки
urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>', get_category, name='category'),
    path('news/<int:news_id>', view_news, name='view_news'),
]
