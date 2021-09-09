from django.shortcuts import render, redirect
from .models import *
from .forms import IndexForm
from django.contrib.auth import authenticate,login,logout
from subscribe.forms import *
from subscribe.models import Subscribe as Subscribe2
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    index = Index.objects.all()
    sub = Subscribe2.objects.all()
    # İndex.object.filter(is_activate=True).all()
    context = {
        'index': index,
        "sub" : sub,
    }
    return render(request, 'index.html', context)






def index_detail(request,slug):
    index = Index.objects.get(slug=slug)
    index.count += 1
    index.save()
    context = {
        'index': index,

    }
    return render(request, 'index_detail.html', context)

def create(request):
    form = IndexForm()
    if request.method == "POST":
        form = IndexForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def update(request, id):
    index = Index.objects.get(id=id)
    if index.user == request.user:
        form = IndexForm(instance=index)
        if request.method == "POST":
            form = IndexForm(request.POST, instance=index)
            if form.is_valid():
                form.save()
                return redirect('core:index')
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def delete(request, id):
    index = Index.objects.get(id=id)
    if index.user == request.user:
        if request.method == "POST":
            index.delete()
            return redirect('core:index')
    context = {
        'x': index
    }
    return render(request, 'delete.html', context)




def subscribe(request):
    if request.method == 'POST':
        form =  SubscribeForms(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            email = obj.email
            from_email = settings.EMAIL_HOST_USER
            to = [email]
            send_mail("Subscribe succesfully","You subscribe succesfully. We send announcment. Thanks!",from_email,to)
            return redirect('/')
    return redirect('/')


