from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')



def structure(request):
    return render(request, 'structure.html')
