from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', index, name = "index"),
    path('home/', HomeView.as_view(), name ="home"),
    path('description/<slug:card_slug>/', DescriptionView.as_view(), name ="description"),
    path('us/', UsView.as_view(), name="us"),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('cart/',cart, name='cart'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/',RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('add/<int:card_id>/<str:size>/', cart_add, name='cart_add'),
    path('del/<int:card_id>/', card_delete, name='card_delete'),
]