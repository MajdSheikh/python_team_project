from django.shortcuts import render, redirect
from carchive_app.models import *
from django.contrib import messages
import bcrypt
from datetime import datetime
from django.core.files.storage import FileSystemStorage


# Create your views here.
def showroom_login(request):
    if 'showroom_id' in request.session:
        return redirect('/dashboard/')
    return render(request,'showroom_login.html')

def showroom_logout(request):
    if 'showroom_id' in request.session:
        del request.session['showroom_id']
    return redirect('/')

def showroom_logged_in(request):
    if not 'showroom_id' in request.session:
        return False
    else:
        return True

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

def cars_dashboard(request):
    if not showroom_logged_in(request):
        return redirect('/')
    context={
        "cars":Showroom.objects.get(id=request.session['showroom_id']).cars.all()
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

def create_car(request):
    if not showroom_logged_in(request):
        return redirect('/')
    if request.method == 'POST':
        model=BrandModel.objects.get(id=request.POST['model'])
        showroom=Showroom.objects.get(id=request.session['showroom_id'])
        prod_date=request.POST['prod_date']
        color=request.POST['color']
        vin=request.POST['vin']
        Car.objects.create(model=model,showroom=showroom,prod_date=prod_date,color=color,vin=vin)
        return redirect('/dashboard/')
    return redirect('/dashboard/')


def edit_car(request,id):
    if not showroom_logged_in(request):
        return redirect('/')
    car=Car.objects.get(id=id)
    car_prod_date=datetime.strftime(car.prod_date,'%Y-%m-%d')
    if not car in Showroom.objects.get(id=request.session['showroom_id']).cars.all():
        return redirect('/')
    context={
        'car':car,
        'brands':Brand.objects.all(),
        'models':BrandModel.objects.all(),
        'car_prod_date':car_prod_date,
    }

    return render(request,'edit_car.html',context)

def update_car(request,id):
    if not showroom_logged_in(request):
        return redirect('/')
    if request.method == 'POST':
        try:
            car=Car.objects.get(id=id)
        except:
            return redirect('/')
        else:
            model=BrandModel.objects.get(id=request.POST['model'])
            prod_date=request.POST['prod_date']
            color=request.POST['color']
            vin=request.POST['vin']
            car.model=model
            car.prod_date=prod_date
            car.color=color
            car.vin=vin
            car.save()
            return redirect('/show_car/'+str(car.id)+'/')
    return ('/')
    
def show_car(request,id):
    if not showroom_logged_in(request):
        return redirect('/')
    car=Car.objects.get(id=id)
    if not car in Showroom.objects.get(id=request.session['showroom_id']).cars.all():
        return redirect('/')
    context={
        'car':car,
        'doc_types':DocumentType.objects.all(),
    }
    return render(request,'show_car.html',context)


def upload_doc(request,id):
    if request.method == 'POST':
        uploaded_file=request.FILES['document']
        doc_type_id = request.POST['doc_type']
        doc_type=DocumentType.objects.get(id = doc_type_id)
        car=Car.objects.get(id=id)
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        # fs=FileSystemStorage()
        # fs.save(uploaded_file.name,uploaded_file)
        Document.objects.create(car=car,type=doc_type,doc=uploaded_file)



    return redirect('/show_car/'+str(id)+'/')