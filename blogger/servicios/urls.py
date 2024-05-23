from django.urls import path
from .views import *

from .views import *

urlpatterns = [
    path('index_servicios/', index_servicios, name='index_servicios'),
]
