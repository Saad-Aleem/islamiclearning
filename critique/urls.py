from django import urls
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='critique'),
    path('/blogpost/<int:id>', views.blogpost, name='blogpost')
]