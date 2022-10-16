from django import template
from news.models import Category

register = template.Library()

# кастомные теги для вывода
@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('news/list_categories.html')
def show_category():
    categories = Category.objects.all()
    return {"categories": categories}
