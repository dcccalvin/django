from django.urls import path
from . import views

urlpatterns = [
    path("newyear",views.newyear),
    path("",views.newyear),
    path("show",views.page),
]