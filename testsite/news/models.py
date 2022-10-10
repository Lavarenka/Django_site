from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')  # blank - не обязательно к заполнению
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True,
                                 verbose_name='Категория')
    # on_delete настройкад для удаления категории PROTECT защита от удаления
    #default для всех записей номер категории 1
    # рекомендуется добавить поле с цитатой

    # для ссылок:
    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})

    # выводим нормальное описание title
    def __str__(self):
        return self.title

    # Наименование модели в админке
    class Meta:
        verbose_name = 'Новость'  # ед число
        verbose_name_plural = 'Новости'  # мн число
        ordering = ['-created_at']  # sort


# Создаем категории
class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True,
                             verbose_name='Наименование категории')  # db_index индексирует поле

    # для ссылок:
    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'  # ед число
        verbose_name_plural = 'Категории'  # мн число
        ordering = ['title']  # sort
