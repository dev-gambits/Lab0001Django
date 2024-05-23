from django.shortcuts import render

# Create your views here.


def index_contacto(request):
    view_templates = 'contacto.html'
    return render(request, view_templates)