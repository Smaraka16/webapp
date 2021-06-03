from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from hello import views
 

app_names = ' hello'
urlpatterns = [
     
    path('login', views.loginuser, name='login'),
    path('', views.index, name='home'),
    path('about.html', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('logout', views.logoutuser, name='logout'),
    path('book',views.books,name='lib'),
    path('sign', views.register,name='sign')
     
     
     
     

]