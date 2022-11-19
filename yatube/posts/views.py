from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    template = 'posts/index.html'
    context = {
        'posts': posts,
        }
    return render(request, template, context)


def group_posts_list(request):
    title = "Здесь будет информация о группах проекта Yatube"
    template = 'posts/group_list.html'
    context = {'title': title}
    return render(request, template, context)


def group_posts(request, slug):
    return HttpResponse(f'Номер страницы сообщества {slug}')
