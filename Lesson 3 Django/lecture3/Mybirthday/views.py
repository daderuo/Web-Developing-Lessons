from django.shortcuts import render

import  datetime
# Create your views here.

def index(request):

    now = datetime.datetime.now()

    return render(request, "Mybirthday\index.html", {
        "birthday": now.day == 21 and now.month == 8
    })
