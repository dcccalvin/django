import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def newyear(show):
    return HttpResponse("New year page")
def page(request):
    now = datetime.datetime
    return render(request,"New_Year.html",{
        "new": now.month == 1 and now.day == 1
    })