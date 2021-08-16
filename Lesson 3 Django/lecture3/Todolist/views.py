from django.shortcuts import render

Todo = ["wake up", "eat", "sleep"]

# Create your views here.
def index(request):
    return render(request, "Todolist/index.html", {
        "Todo": Todo
    })

def add(request):
    return render(request, "Todolist/add.html")