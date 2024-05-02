from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User



# Create your views here.


def user_login(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            print("giriş",user)
            return redirect("index")    
        else:
            return render(request,"user/login.html",{"error":"Invalid Username or Password"})
        
    return render(request,'user/login.html')



def user_register(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        
        if password == repassword:
            if User.objects.filter(username = username).exists():
                return render(request,'user/register.html',
                              {"error":"There Is Already A User Who Uses This Username , So Please Register Using Another Username",
                               "username":username,
                               "email":email,
                               "firstname":firstname,
                               "lastname":lastname,
                               })
            else:
                if User.objects.filter(email = email).exists():
                    return render(request,'user/register.html',
                                  {"error":"There Is Already A User Who Uses This Email , So Please Register Using Another Email",
                                   "username":username,
                                   "email":email,
                                   "firstname":firstname,
                                   "lastname":lastname,
                                    })
                else:
                    User.objects.create_user(username = username , email = email , first_name = firstname , last_name = lastname , password = password)
                    
                    return redirect("login")
                    
        else:
            return render(request,'user/register.html',
                          {"error":"Password and Re-Password doesn't match",
                           "username":username,
                           "email":email,
                           "firstname":firstname,
                           "lastname":lastname,
                           })
        
        
    return render(request,'user/register.html')



def user_logout(request):
    logout(request)
    return redirect("index")