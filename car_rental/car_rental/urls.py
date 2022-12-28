"""car_rental URL Configuration

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
from django.urls import path, include
from rent.views import homepage, sport, suv, exotic, sedan, rent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', homepage, name='homepage'),
    path('homepage/sport/', sport, name='sport'), 
    path('homepage/suv', suv, name='suv'),
    path('homepage/exotic', exotic, name='exotic'),
    path('homepage/sedan', sedan, name='sedan'),
    path('homepage/rent/<int:pk>', rent, name='rent'),
]