from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('login/', login, name='login'),
    path('portafolio/', portafolio, name='portafolio'),

    path('', include('nosotros.urls')),
    path('', include('blog.urls')),
    path('', include('contacto.urls')),
    path('', include('productos.urls')),
    path('', include('servicios.urls')),
]
