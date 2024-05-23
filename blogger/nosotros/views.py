from django.shortcuts import render

# Create your views here.


def index_nosotros(request):
    view_templates = 'nosotros.html'
    return render(request, view_templates)