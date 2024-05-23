from django.shortcuts import render

# Create your views here.


def index_servicios(request):
    view_templates = 'servicios.html'
    return render(request, view_templates)