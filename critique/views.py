from typing_extensions import ParamSpec
from django.shortcuts import render
from .models import develop
# Create your views here.
def index(request):
    posts = develop.objects.all()
    return render(request,'critique/critique.html', {'posts':posts})

def blogpost(request, id):
    post = develop.objects.filter(id = id)[0]
    return render(request, 'critique/blog.html', {'post': post})