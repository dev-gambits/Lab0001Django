from django.urls import path
from .views import *

urlpatterns = [
    path('index_contacto/', index_contacto, name='index_contacto'),
]
