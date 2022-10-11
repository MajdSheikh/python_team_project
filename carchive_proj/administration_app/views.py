from django.shortcuts import render, redirect
from administration_app.models import Admin
from carchive_app.models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def admins_login(request):
    return render(request,'admins_login.html')

def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        print(email)
        try:
            admin=Admin.objects.get(email=email)
        except:
            messages.error(request,'Account Does Not Exist')
            print("user does not exist")
            return redirect('/admin/')
        else:
            if bcrypt.checkpw(str(password).encode(), str(admin.password).encode()):
                request.session['id'] = admin.id
                return redirect('/admin/dashboard/')
            else:
                return redirect('/admin/')
    
    
def logout(request):
    if 'id' in request.session:
        del request.session['id']
    return redirect('/admin/')

def admin_dashboard(request):
    context={
        'showrooms':Showroom.objects.all()
    }
    return render(request,'admin_dashboard.html',context)

def add_showroom(request):
    return render(request,'add_showroom.html')

def edit_showroom(request,id):
    return render(request,'edit_showroom.html')

def add_items(request):
    return render(request,'add_items.html')