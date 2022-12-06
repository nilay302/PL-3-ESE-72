from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.HomePage,name="HomePage"),
    path('studentRegister',views.StudentRegister,name="StudentRegister"),
    path('studentForm',views.BonafideForm,name="Bonafide"),
    path('adminLogin',views.AdminLogin,name="AdminLogin"),
    path('adminpage',views.AdminPage,name = "AdminPage"),
    path('studentLogin',views.StudentLogin,name="StudentLogin"),
]