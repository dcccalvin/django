from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.

def xmas(request):
    now = datetime.datetime.now()
    return render(request,"xmas_show.html", {
        "new":now.month == 4 and now.day == 4
    })