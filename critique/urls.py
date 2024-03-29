from django import urls
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='critique'),
    path('/blogpost/<int:id>', views.blogpost, name='blogpost')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
