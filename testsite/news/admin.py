from django.contrib import admin
from .models import News, Category


# настройки админки
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','category', 'created_at', 'updated_at', 'is_published')  # поля для отображения в админке
    list_display_links = ('id', 'title')  # наименования которые будут ссылкой в админ
    search_fields = ('title', 'content')  # поиск по полям
    list_editable = ('is_published',) # редактирование прямо из списка
    list_filter = ('is_published', 'category') # фильтр в админке


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')  # поля для отображения в админке
    list_display_links = ('id', 'title')  # наименования которые будут ссылкой в админ
    search_fields = ('title',)  # поиск по полям


# регистрируем приложуху в админке и настройки
# порядок важен!
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
