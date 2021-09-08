from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login

# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username =username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        # messages.info(request,"Başarıyla Kayıt Oldunuz...")

        return redirect("index")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)


def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)
        if user is None:
            return render(request,"login.html",context)

        login(request,user)
        
        return redirect("core:index")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    return redirect("core:index")

