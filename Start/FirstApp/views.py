from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")#render function shows a particular file
def hello(request):
    return HttpResponse("Thank you for visiting this website")
def custom(request):
    return HttpResponse("You got it right")
def emobilis(request):
    return HttpResponse("welcome to emobilis")