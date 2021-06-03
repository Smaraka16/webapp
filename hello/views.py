from django.shortcuts import render,redirect, HttpResponse, Http404
from django.conf import settings
from django.http import response
from datetime import datetime
from hello.models import Contact, Books
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from django.views import generic
from django.urls import reverse_lazy

import os

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email = request.POST['email']
        phone = request.POST['phone']

        # check for errorneous inputs
        


             


        # create user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'good job')
        return redirect('/login')
    else:
        return render(request,'sign.html')    

     
     
            
    return render(request,'sign.html')



def index(request):
    if request.user.is_anonymous:
        return redirect('/login')

    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def loginuser(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect('/login')


 
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone,
                          message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'your request has been sent!!')
    return render(request, 'index.html')


def books(request):
    context = {'file': Books.objects.all()}
    return render(request, 'book.html', context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response = HttpResponse(fh.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=' + \
                os.path.basename(file_path)
            return response

    raise Http404
