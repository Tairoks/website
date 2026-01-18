from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная свяь', 'url_name': 'contacts'},
    {'title': 'Войти', 'url_name': 'login'},
        ]

def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, "women/index.html", context=context)

def about(request):
    context = {
        'title': 'О сайте',
        'menu': menu
    }
    return render(request, 'women/about.html', context=context)

def categories(request, catid):
    return HttpResponse(f"<h1>Категория</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2025:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def add_page(request):
    return HttpResponse("Добавление статьи")

def contacts(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Логин")

def show_post(request, post_id):
    return HttpResponse(f'ID статьи{post_id}')

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, "women/index.html", context=context)
