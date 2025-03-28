from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import tbl_Course


# Create your views here.
def login_User(request):
    login_status=False
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)

        if user is not None:
             login(request,user)
             return redirect('/Main/')
        else:
            messages.warning(request, 'Invalid username or password')
            return redirect('/',messages)
   
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
        if C==D:
            if not user_data_error:
                new_user = User.objects.create_user(
                email = B,
                username = A,
                password = C,
                
            )
                messages.success(request,'Account created. Login now')
                return redirect('/',messages)
            else:
                return redirect('/Register/')
        else:
            messages.warning(request,'Password not matching')  


    return render(request,'register.html')

@login_required
def main(request):
    course=tbl_Course.objects.all()
    return render(request,'index.html',{'c':course})
def Course(request):
    return render(request,'viewmore.html')

