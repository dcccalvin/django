from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="hello"),#nothing btwn the "" opens views.hello as default
    path("calvin", views.custom, name="custom"),
    path("emobilis", views.emobilis, name="emobilis"),
    path("home", views.home,)

]
