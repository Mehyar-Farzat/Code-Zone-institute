from django.shortcuts import render, redirect
from django.contrib import messages
import re
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.



def signup(request):
    flag=0
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        # print(name,email,password,confirm_password)
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return redirect('/auth/signup/') 
        if len(password)<=5:
            messages.warning(request,"Password must be atleast 5 character")
            return redirect('/auth/signup/') 
        elif not re.search("[a-z]", password):
            flag = -1
            
        elif not re.search("[A-Z]", password):
            flag = -1
            
        elif not re.search("[0-9]", password):
            flag = -1
            
        elif not re.search("[_@$#%^*()-]" , password):
            flag = -1  
        else:
            pass

        if(flag==0):
            try:
                if User.objects.get(username=email):
                # return HttpResponse("email already exist")
                    messages.success(request,"Email is Taken")
                    return redirect('/auth/signup/')

            except Exception as identifier:
                pass

            user = User.objects.create_user(email,email,password)
            user.first_name=name
            user.is_active=False
            user.save()
            messages.success(request,"signup success please login")
            return redirect('/auth/login/')

            

        else:
            messages.error(request,"Password is not valid")
            return redirect('/auth/signup/') 
        


    return render(request,"signup.html")
        
     
        
    

def handleLogin(request):
    return render(request, 'login.html')

def handleLogout(request):
    return render(request, 'logout.html')