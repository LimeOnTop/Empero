from django.urls import path

from .views import *

urlpatterns = [
    path('Emprero.html', index),
    path('purchase.html', description),
]