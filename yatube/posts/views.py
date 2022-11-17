from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    return render(request, template)


def group_posts_list(request):
    return HttpResponse('Список страниц')


def group_posts(request, slug):
    return HttpResponse(f'Номер страницы сообщества {slug}')
