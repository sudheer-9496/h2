from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Product
from django.contrib.auth.models import User , auth
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def garden_view(request):
    return render(request, 'garden.html')

def furniture_view(request):
    return render(request, 'furniture.html')

def fruits_list(request):
    return render(request, 'fruitslist.html')
def payment_list(request):
    return render(request, 'payment.html')


def login(request):
    if request.method =='POST' :
         username =request.POST['username']
         password =request.POST['password']

         user= auth.authenticate(username=username,password=password)

         if user is not None:
              auth.login(request, user)
              redirect("/index")
              
    else:
        return render(request,'login.html')     
    

def register(request):
    if request.method =='POST' :
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
            else:
                myuser= User.objects.create_user(first_name=name,username=username,email=email,password=password1)
                myuser.save()    
                return redirect("/")
    else:
        return render(request,'register.html')