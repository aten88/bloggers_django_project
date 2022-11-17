from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    title = "Это главная страница проекта Yatube"
    template = 'posts/index.html'
    context = {'title': title}
    return render(request, template, context)


def group_posts_list(request):
    title = "Здесь будет информация о группах проекта Yatube"
    template = 'posts/group_list.html'
    context = {'title': title}
    return render(request, template, context)


def group_posts(request, slug):
    return HttpResponse(f'Номер страницы сообщества {slug}')
