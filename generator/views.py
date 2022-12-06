from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages
from . import models
# Create your views here.
def AdminLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('AdminPage')
        else:
             messages.error(request,'Login Failed')
    return render(request,'generator/adminLogin.html',{})

@login_required(login_url=AdminLogin)
def AdminPage(request):
    return render(request,'generator/AdminPage.html',{})

def StudentLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('Bonafide')
        else:
             messages.error(request,'Login Failed')
    return render(request,'generator/studentLogin.html',{})

def HomePage(request):
    return render(request,'generator/home.html',{})

def StudentRegister(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created')
            return redirect('HomePage')
    context = {'form':form}
    return render(request,'generator/StudentRegister.html',context)

def BonafideForm(request):
    if request.method == 'POST':
        # id = pk
        Name = request.POST.get('name')
        Class = request.POST.get('class')
        year = request.POST.get('year')
        reason = request.POST.get('reason')
        form = models.Bonafide(id,Name,Class,year,reason)
        form.save()
        return redirect('HomePage')
    return render(request,'generator/StudentForm.html',{})