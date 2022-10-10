from django.shortcuts import render

# Create your views here.
def admins_login(request):
    return render(request,'admins_login.html')

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

def add_showroom(request):
    return render(request,'add_showroom.html')

def edit_showroom(request,id):
    return render(request,'edit_showroom.html')

def add_items(request):
    return render(request,'add_items.html')