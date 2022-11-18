# posts/urls.py
from django.urls import path

from . import views
app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('group/', views.group_posts_list, name='group_posts_list'),
    path(
        'group/<slug:slug>/',
        views.group_posts
    ),
]
