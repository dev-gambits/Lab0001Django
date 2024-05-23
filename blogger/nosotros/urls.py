from django.urls import path
from .views import *

urlpatterns = [
    path('index_nosotros/', index_nosotros, name='index_nosotros'),
]
