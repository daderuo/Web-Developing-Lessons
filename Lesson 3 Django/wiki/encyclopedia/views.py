from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

from . import util


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
    

def show(request, Title = None):
    Content = util.get_entry(Title)
    if Content == None:
        Title = "Error"
        Content = "Error 404 Page not found!"
    return render(request, "encyclopedia/show.html", {
        "Title" : Title,
        "ToShow" : Content
    })
