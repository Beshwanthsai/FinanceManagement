
from django.shortcuts import render, redirect


# Create your views here.
def homepagecall(request):
    return render(request, 'adminapp/projecthomepage.html')

def Loginpagecall(request):
    return render(request,'adminapp/Login.html')

def Registerpagecall(request):
    return render(request,'adminapp/Register.html')