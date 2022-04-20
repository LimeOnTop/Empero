from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST

from .forms import RegisterUserForm, LoginUserForm, SizeForm
from .models import *
from django.views.generic import ListView, DetailView, CreateView, FormView
from .cart import SessionCart
from django.conf import settings

library = [{'title': 'Home'},
           {'title': 'Description'},
           {'title': 'About us'},
           {'title': 'Contacts'},
           {'title': 'Cart'}]


def index(request):
    return redirect('home')


class HomeView(ListView):
    model = Clothes
    template_name = 'main/home.html'
    context_object_name = 'cards'
    extra_context = {'title': 'Home'}
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['library'] = library
        return context


@require_POST
def cart_add(request, card_id):
    cart = SessionCart(request)
    form = SizeForm(request.POST)
    if form.is_valid():
        product = get_object_or_404(Clothes, id=card_id)
        cart.add(product=product, size= form.cleaned_data['size'])
        if 'buy' in request.POST:
            return redirect('cart')
        else:
            return redirect(request.META.get('HTTP_REFERER'))


def card_delete(request, card_id):
    cart = SessionCart(request)
    product = get_object_or_404(Clothes, id=card_id)
    cart.remove(product=product)
    return redirect('cart')


class DescriptionView(DetailView, FormView):
    model = Clothes
    form_class = SizeForm
    slug_url_kwarg = 'card_slug'
    template_name = 'main/description.html'
    context_object_name = 'card'
    extra_context = {'title': 'Description'}


class UsView(ListView):
    model = Clothes
    template_name = 'main/us.html'
    extra_context = {'title': 'About us'}


class ContactsView(ListView):
    model = Clothes
    template_name = 'main/contacts.html'
    extra_context = {'title': 'Contacts'}


def cart(request):
    cart = SessionCart(request)
    total_price = cart.total_price()
    return render(request, 'main/cart.html', {'title': 'Cart', 'cart': cart, 'total_price': total_price})


class LoginView(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'
    extra_context = {'title': 'Login'}


class RegisterView(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    extra_context = {'title': 'Register'}
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class ProfileView(DetailView):
    model = User
    template_name = 'main/profile.html'
    context_object_name = 'user'
    extra_context = {'title': 'Profile'}
