from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('Hello wotrld')

def test(request):
    return HttpResponse('<H1>Тестовая старница<>')


