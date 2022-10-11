from django.shortcuts import render
from carchive_app.models import *
# Create your views here.
def showroom_login(request):
    return render(request,'showroom_login.html')

def cars_dashboard(request):
    context={
        "cars":Car.objects.all()
    }
    return render(request,'cars_dashboard.html',context)

def add_new_car(request):
    return render(request,'add_new_car.html')

def edit_car(request,id):
    return render(request,'edit_car.html')

def show_car(request,id):
    return render(request,'show_car.html')