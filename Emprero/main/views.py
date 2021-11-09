from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, DetailView

library = [{'title': 'Home'},
           {'title': 'Description'},
           {'title': 'About us'},
           {'title': 'Contacts'},
           {'title': 'Cart'}]


def index(request):
    return redirect('home')


class Home(ListView):
    model = Clothes
    template_name = 'main/home.html'
    context_object_name = 'cards'
    extra_context = {'title': 'Home'}
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['library'] = library
        return context


class Description(DetailView):
    model = Clothes
    slug_url_kwarg = 'card_slug'
    template_name = 'main/description.html'
    context_object_name = 'card'
    extra_context = {'title': 'Description'}


class Us(ListView):
    model = Clothes
    template_name = 'main/us.html'
    extra_context = {'title': 'About us'}


class Contacts(ListView):
    model = Clothes
    template_name = 'main/contacts.html'
    extra_context = {'title': 'Contacts'}


class Cart(ListView):
    model = Clothes
    template_name = 'main/cart.html'
    context_object_name = 'cards'
    extra_context = {'title': 'Cart'}

    def get_queryset(self):
        return Clothes.objects.filter(picked=True)


def register(request):
    # form = RegisterForm()
    return
