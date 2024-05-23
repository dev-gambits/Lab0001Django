from django.urls import path
from .views import *

urlpatterns = [
    path('index_blog/', index_blog, name='index_blog'),
]
