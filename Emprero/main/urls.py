from django.urls import path

from .views import *

urlpatterns = [
    path('home', home, name = "home"),
    path('description', description, name = "description"),
    path('us', us, name="us"),
]