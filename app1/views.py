from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout
from django.contrib import messages


# Create your views here.
def login(request):
   
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        A=request.POST['Name']
        B=request.POST['Email']
        C=request.POST['Pass']
        D=request.POST['Cpass']
        
        user_data_error=False
        if User.objects.filter(username=A).exists():
            user_data_error=True
            messages.warning(request,'Username already exists')
        if User.objects.filter(email=B).exists():
            user_data_error = True
            messages.warning(request, 'Email already exists')
        if len(C) < 5:
            user_data_has_error = True
            messages.warning(request, 'Password must be at least 5 characters')

        if not user_data_error:
            new_user = User.objects.create_user(
            email = B,
            username = A,
            password = C
        )
            messages.success(request, 'Account created. Login now')
            return redirect('/')
        else:
            return redirect('/Register/')
        


    return render(request,'register.html')


