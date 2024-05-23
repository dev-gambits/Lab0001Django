from django.urls import path
from .views import *

from .views import *

urlpatterns = [
    path('index_productos/', index_productos, name='index_productos'),
]
