# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/', views.group_posts_list),
    path(
        'group/<slug:slug>/',
        views.group_posts
    ),
]
