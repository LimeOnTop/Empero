from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'main/Emprero.html', {'title': 'Home'})


def description(request):
    return render(request, 'main/purchase.html', {'title': 'Description'})
