from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import RegisterUserForm, LoginUserForm
from .models import *
from django.views.generic import ListView, DetailView, CreateView

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
    paginate_by = 6

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


def check_sum():
    summary_price = 0
    for card in Clothes.objects.filter(picked=True):
        summary_price += card.price
    return summary_price


class Cart(ListView):
    model = Clothes
    template_name = 'main/cart.html'
    context_object_name = 'cards'
    extra_context = {'title': 'Cart', 'summary_price': check_sum()}

    def get_queryset(self):
        return Clothes.objects.filter(picked=True)


class Login(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'
    extra_context = {'title': 'Login'}


class Register(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    extra_context = {'title': 'Register'}
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class Profile(DetailView):
    model = User
    # slug_url_kwarg = '???'
    template_name = 'main/profile.html'
    context_object_name = 'user'
    extra_context = {'title': 'Profile'}
