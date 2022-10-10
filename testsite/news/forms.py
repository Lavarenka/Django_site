from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название')
    content = forms.CharField(label='Текст')
    is_published = forms.BooleanField(label='Опубликовано', initial=True) # первоночально чекбокс стоит
    category = forms.ModelChoiceField(label='Категория', queryset=Category.objects.all())