from django.shortcuts import render

# Create your views here.


def index_blog(request):
    view_templates= 'blog.html'
    return render(request, view_templates)