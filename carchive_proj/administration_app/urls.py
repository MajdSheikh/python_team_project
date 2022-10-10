from django.urls import path
from . import views

urlpatterns=[
    path('',views.admins_login),
    path('dashboard/',views.admin_dashboard),
    path('add_showroom/',views.add_showroom),
    path('edit_showroom/<id>/',views.edit_showroom),
    path('add_items/',views.add_items),
]