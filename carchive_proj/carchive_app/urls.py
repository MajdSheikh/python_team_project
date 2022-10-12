from django.urls import path
from . import views

urlpatterns=[
    path('',views.showroom_login),
    path('logging/',views.logging),
    path('logout/',views.showroom_logout),
    path('dashboard/',views.cars_dashboard),
    path('add_new_car/',views.add_new_car),
    path('edit_car/<id>/',views.edit_car),
    path('show_car/<id>/',views.show_car),
] 