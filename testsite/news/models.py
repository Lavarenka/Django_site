from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')  #blank не обязательно к заполнению
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    # выводим нормальное описание title
    def __str__(self):
        return self.title


    # Наименование модели в админке
    class Meta:
        verbose_name = 'Новость' # ед число
        verbose_name_plural = 'Новости' # мн число
        ordering = ['-created_at'] # sort


