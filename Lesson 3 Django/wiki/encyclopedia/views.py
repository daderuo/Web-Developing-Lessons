from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

from . import util

#random function
import random

def Rand(request):
    Entries = util.list_entries()
    entry = Entries[random.randrange(0, len(Entries))]
    return HttpResponseRedirect(reverse('wiki:show', args=(entry,)))

def index(request):
    Entries = util.list_entries()
    result = []

    if request.method == 'GET':
        q = str(request.GET.get('q', ''))
        if q != '':
            for entry in Entries:
                if q == entry:
                    return HttpResponseRedirect(reverse('wiki:show', args=(q,)))
                if q in entry:
                    result.append(entry)
            return render(request, "encyclopedia/index.html", {
                "entries": result
            })
    
    return render(request, "encyclopedia/index.html", {
        "entries": Entries
    })

#Markdown conversion
import markdown2

def show(request, Title = None):
    Content = util.get_entry(Title)    

    if Content == None:
        Title = "Error"
        Content = "Error 404 Page not found!"
    return render(request, "encyclopedia/show.html", {
        "Title" : Title,
        "ToShow" : markdown2.markdown(Content)
    })


#Form creation
from django import forms

class NewEntriesForm (forms.Form):
    title = forms.CharField(label="Title",max_length=50)
    text = forms.CharField(label="Text", widget=forms.Textarea)

def new(request):
    if request.method == 'POST':
        form = NewEntriesForm(request.POST)        

        if form.is_valid():
            Title = form.cleaned_data["title"]
            Content = form.cleaned_data["text"]


            Entries = util.list_entries()
            for entry in Entries:
                if Title == entry:
                    return render(request,"encyclopedia/editor.html",{
                        "title": Title,
                        "form": form,
                        "error": "Error: entry already exist!"
                    })

            util.save_entry(Title, ('# '+ Title + '\n' + Content))
            return HttpResponseRedirect(reverse("wiki:show",args=(Title,)))

    return render(request,"encyclopedia/editor.html",{
        "title": None,
        "form": NewEntriesForm()
    })

    

def edit(request, Title):
    if request.method == 'POST':
        form = NewEntriesForm(request.POST)        

        if form.is_valid():
            Title = form.cleaned_data["title"]
            Content = form.cleaned_data["text"]
            util.save_entry(Title, Content)
            return HttpResponseRedirect(reverse("wiki:show",args=(Title,)))

    Content = util.get_entry(Title)
    Form = NewEntriesForm(initial={'title':Title, 'text':Content})

    return render(request,"encyclopedia/editor.html",{
        "title": Title,
        "form": Form,
        "Edit": 1
    })


