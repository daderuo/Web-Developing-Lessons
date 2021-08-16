from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello\index.html")

def davide(request):
    return HttpResponse("Hello Davide")

def hitoyou(request,name):
    return render(request, "hello\greet.html", {
        "name": name.capitalize()
    })