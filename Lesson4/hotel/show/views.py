from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .models import *

# Create your views here.

def index(request):
    rooms = Hotel.objects.all()
    return render(request, "show/index.html", {
        "rooms": rooms
    })

def available(request):
    rooms = Hotel.objects.filter(available=True)
    return render(request, "show/index.html", {
        "rooms": rooms
    })

def booked(request):
    rooms = Hotel.objects.filter(available=False)
    return render(request, "show/index.html", {
        "rooms": rooms
    })