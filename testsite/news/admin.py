from django.contrib import admin
from .models import News


# настройки админки
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published') # поля для отображения в админке
    list_display_links = ('id', 'title') #наименования которые будут ссылкой в админ
    search_fields = ('title', 'content') #поиск по полям


# регистрируем приложуху в админке и настройки
#порядок важен!
admin.site.register(News, NewsAdmin)
