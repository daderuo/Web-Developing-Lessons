from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from show.models import *

# Create your views here.

def index(request):
    return render(request, "reservations/index.html", {
        "rooms": Hotel.objects.filter(available=True)
    })

def add_guest(request):
    if request.method == "POST":
        first_name = request.POST['first']
        last_name = request.POST['last']
        room_id = int(request.POST['room'])
        room = Hotel.objects.get(id=room_id)
        
        if Guest.objects.filter(first_name=first_name,last_name=last_name):
            guest = Guest.objects.get(first_name=first_name,last_name=last_name)
        else:
            guest = Guest(first_name=first_name,last_name=last_name)
            guest.save()

        guest.booked_room.add(room)
        
        room.available = False
        room.save()
        
        return HttpResponseRedirect(reverse("reservations:guest", args=(guest.id,)))
    
    return render(request, "reservations/index.html", {
        "rooms": Hotel.objects.filter(available=True)
    })

def guest(request, guest_id):
    g = Guest.objects.get(pk=guest_id)
    guest = Guest.objects.get(first_name= g.first_name,last_name=g.last_name)
    booked_room = []
    return render(request, "reservations/guest.html", {
        "guest": g,
        "booked_room": guest.booked_room.all()
    })
    return HttpResponse(g)

