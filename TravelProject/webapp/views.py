# Create your views here.

from django.shortcuts import render, redirect
from .models import Place
from .models import Team


def news(request):
    return render(request, 'news.html')


def home(request):
    obj = Place.objects.all()  # ORM form
    team = Team.objects.all()
    return render(request, "index.html", {'result': obj, 'team': team})



def elements(request):
    return render(request, 'elements.html')


def contact(request):
    return render(request,'contact.html')


def destinations(request):
    return render(request,'destinations.html')