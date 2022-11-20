from django.shortcuts import render, get_object_or_404
from .models import Post, Group


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
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }

    return render(request, 'posts/group_list.html', context)
