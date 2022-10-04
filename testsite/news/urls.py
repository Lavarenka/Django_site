from django.urls import path, include
from .views import *
# подключаем страницчки
urlpatterns = [
    path('', index),
]
