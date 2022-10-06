from django.urls import path, include
from .views import *
# подключаем страницчки
urlpatterns = [
    path('', index),
    path('category/<int:category_id>', get_category),
]
