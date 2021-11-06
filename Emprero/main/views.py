from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def home(request):
    cards = Clothes.objects.all()
    return render(request, 'main/home.html', {'title': 'Home', 'cards': cards})


def description(request):
    return render(request, 'main/description.html', {'title': 'Description'})


def us(request):
    return render(request, 'main/us.html', {'title': 'About us'})
