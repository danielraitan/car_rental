from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import CarInfo
from django.core.mail import send_mail

# Create your views here.

def homepage(request):
    cars = CarInfo.objects.all()

    context = {
        'cars': cars
    }

    return render(request, 'index.html', context)

def sport(request):
    cars = CarInfo.objects.all()

    context = {
        'cars': cars
    }
    return render(request, 'sport.html', context)

def suv(request):
    cars = CarInfo.objects.all()

    context = {
        'cars': cars
    }
    return render(request, 'suv.html', context)

def exotic(request):
    cars = CarInfo.objects.all()

    context = {
        'cars': cars
    }
    return render(request, 'exotic.html', context)

def sedan(request):
    cars = CarInfo.objects.all()

    context = {
        'cars': cars
    }
    return render(request, 'sedan.html', context)

def rent(request, pk):
    
    cars = CarInfo.objects.get(id=pk)
    form = UploadForm()

    context = {
        'cars': cars, 'form': form
    }
    
    if request.method=='POST':
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
        
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect(homepage)
    
        
    return render(request, 'rent.html', context)
