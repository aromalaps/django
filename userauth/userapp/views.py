from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django. contrib import auth

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
               return redirect('register')     
           elif User.objects.filter(email=email).exists():
                print(" email already exist")
                return redirect('register')         
           else:
               user = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)
               user.save()    
               redirect('Login')
        else:
            print('password not matching')
            return redirect('register')
    return render(req,'register.html')

def login(req):
    if req.method=='POST':
        username=req.POST.get("username","")
        password=req.POST.get("password","")
        user=auth.authenticate(username=username,password=password)
        if user is not None:
          auth.login(req,user)
          print(user)
          req.session['user']=str(user)
          return redirect("home")
        else:
            print("invalid")
            return redirect('Login')
    return render(req,'login.html')
def logout(req):
    auth.logout(req)
    req.session.pop('user',None)
    return redirect('home')
