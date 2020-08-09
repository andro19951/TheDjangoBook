from django.shortcuts import render
import datetime
# Create your views here.

def index(request):
    now = datetime.datetime.now()
    var = now.day==1 and now.month == 1
    return render(request, "newYear/index.html",{
        "newyear": var
        })
    