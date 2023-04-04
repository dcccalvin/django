"""Start URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include #include represents

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello", include("FirstApp.urls")), #This directs youy to the urls in FirstApp
    path("stop", include("FirstApp.urls")),
    path("calvin", include("FirstApp.urls")),
    path("emobilis", include("FirstApp.urls")),
    path("newyear", include("newyear.urls")),
    path("", include("newyear.urls")),
    path("show/", include("newyear.urls")),
    path("xmas/",include("xmas.urls"))

]
