from django.urls import path
from . import views
urlpattern = [
    path('', view.index, name = 'index'),
]