from django.shortcuts import render

# Create your views here.


def index(request):
    view_templates = 'index.html'
    return render(request, view_templates)


def portafolio(request):
    view_templates = 'index.html'
    return render(request, view_templates)


def login(request):
    view_templates = 'index.html'
    return render(request, view_templates)