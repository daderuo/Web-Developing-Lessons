from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Ciao, Mondo! Questa è la homepage dell'app poll")
