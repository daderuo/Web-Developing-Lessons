from django import forms
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

class NewTaskForm(forms.Form):
    NewTask = forms.CharField(label="Write new task")

class RemoveTaskForm(forms.Form):
    Remove = forms.CharField(label="Removed")

# Create your views here.
def index(request):
    if "Todo" not in request.session:
        request.session["Todo"] = []
    return render(request, "Todolist/index.html", {
        "Todo": request.session["Todo"]
    })

def add(request):
    if request.method == "POST":
        saved_data = NewTaskForm(request.POST)

        if saved_data.is_valid():
            new = saved_data.cleaned_data["NewTask"]
            list = request.session["Todo"]
            list.append(new)
            request.session["Todo"] = list
            return HttpResponseRedirect(reverse("task:index"))
        
        else:
            return render(request, "Todolist/add.html", {
                "form":saved_data
            })

    return render(request, "Todolist/add.html", {
        "form" : NewTaskForm()
    })

def remove(request):
    if request.method == "POST":
        data = RemoveTaskForm(request.POST)

        if data.is_valid():
            new = data.cleaned_data["Remove"]
            list = request.session["Todo"]
            list.remove(new)
            request.session["Todo"] = list

            return HttpResponseRedirect(reverse("task:index"))
        
        else:
            return render(request, "Todolist/remove.html", {
                "form":data
            })

    return render(request, "Todolist/remove.html", {
        "Todo": request.session["Todo"]
    })