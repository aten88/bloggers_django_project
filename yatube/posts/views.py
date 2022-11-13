from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts_list(request):
    return HttpResponse('Список страниц')


def group_posts(request, slug):
    return HttpResponse(f'Номер страницы сообщества {slug}')
