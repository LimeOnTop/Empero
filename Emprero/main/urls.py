from django.urls import path

from .views import *

urlpatterns = [
    path('/', index, name = "index"),
    path('home/', Home.as_view(), name = "home"),
    path('description/<slug:card_slug>/', Description.as_view(), name = "description"),
    path('us/', Us.as_view(), name="us"),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('cart/', Cart.as_view(), name='cart'),
]