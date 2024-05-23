from django.shortcuts import render

# Create your views here.


def index_productos(request):
    view_templates = 'productos.html'
    return render(request, view_templates)