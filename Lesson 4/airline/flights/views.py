from django.shortcuts import render

from .models import Flight

from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("ciao")
    return render(request,"flights/index.html",{
        "Flights" : Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    passengers = flight.passenger.all()
    return render(request, "flights/flight.html",{
        "flight": flight,
        "passengers": passengers
    })


