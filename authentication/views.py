from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def home(request):
    return render(request, 'authentication/index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        myuser = User.objects.create_user(username,email,password)
        myuser.firstname = firstname
        myuser.lastname = lastname

        myuser.save()

    return render(request, 'authentication/signup.html')

def signin(request):
    return render(request, 'authentication/signin.html')    

def signout(request):
    pass
