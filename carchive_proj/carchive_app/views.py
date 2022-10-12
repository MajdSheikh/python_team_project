from django.shortcuts import render, redirect
from carchive_app.models import *
from django.contrib import messages
import bcrypt
# Create your views here.
def showroom_login(request):
    if 'showroom_id' in request.session:
        return redirect('/dashboard/')
    return render(request,'showroom_login.html')

def logging(request):
    if request.method == 'POST':
        license=request.POST['license']
        email=request.POST['email']
        password=request.POST['password']
        try:
            showroom=Showroom.objects.get(email=email)
        except:
            messages.error(request,'Account Does Not Exist')
            print("user does not exist")
            return redirect('/')
        else:
            if bcrypt.checkpw(str(password).encode(), str(showroom.password).encode()):
                request.session['showroom_id'] = showroom.id
                return redirect('/dashboard/')
            else:
                return redirect('/')
    else:
        return ('/')

def showroom_logout(request):
    if 'showroom_id' in request.session:
        del request.session['showroom_id']
    return redirect('/')

def showroom_logged_in(request):
    if not 'showroom_id' in request.session:
        return False
    else:
        return True

def cars_dashboard(request):
    if not showroom_logged_in(request):
        return redirect('/')
    context={
        "cars":Car.objects.all()
    }
    return render(request,'cars_dashboard.html',context)

def add_new_car(request):
    if not showroom_logged_in(request):
        return redirect('/')
    context={
        'brands':Brand.objects.all(),
        'models':BrandModel.objects.all(),
    }
    return render(request,'add_new_car.html',context)

def edit_car(request,id):
    if not showroom_logged_in(request):
        return redirect('/')
    return render(request,'edit_car.html')

def show_car(request,id):
    if not showroom_logged_in(request):
        return redirect('/')
    return render(request,'show_car.html')