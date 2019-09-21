from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'] , password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
            #return render(request, 'accounts/login.html',{'error':'Success'})        
        else:
            return render(request, 'accounts/login.html',{'error':'Username or password is incorrect.!'})        
    return render(request, 'accounts/login.html')

def dashboard(request):
    return render(request, 'home.html')

