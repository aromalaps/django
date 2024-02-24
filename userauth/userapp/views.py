from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
def Home(req):
    return render(req,'index.html')
def Register(req):
    if req.method=='POST':
        fname = req.POST.get("first_name",'')
        lname = req.POST.get("last_name",'')
        email = req.POST.get("email",'')
        username = req.POST.get("username",'')
        password = req.POST.get("password",'')
        cpassword = req.POST.get("cpassword",'')
        if password==cpassword:
           if User.objects.filter(email=email).exists():
               print("email exsist")               
           else:
               user = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)
               user.save()    
               redirect('home')
        else:
            print('password not matching')
    return render(req,'register.html')
def Login(req):
    req
    return()