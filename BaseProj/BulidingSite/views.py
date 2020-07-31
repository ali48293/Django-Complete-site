from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .form import devForm
from .models import addDev
# Create your views here.

def devs(request,id=None):
    
    if request.method == "GET":
        if id == None:
            print("GET method Here")
            form = devForm()
        else:
            # id =2
            update = addDev.objects.get(pk=id)
            form = devForm(instance=update)
        return render(request,"devs.html",{"form":form})      
    else:
        if id == None:
            print("POST method Here")
            form = devForm(request.POST)
        else:
            update = addDev.objects.get(pk=id)
            form = devForm(request.POST,instance=update)
        if form.is_valid():
            form.save()
            return redirect("devsList")
    
def devs_list(request):
    form =  addDev.objects.all()
    return render(request,"devsList.html",{"form":form})


def delete(request,id):
    form = addDev.objects.get(pk=id)
    form.delete()
    return redirect("devsList")




def home(request):
     
    return render(request,"home.html")



def register(request):
            
    if request.method == "POST":
        first_name   = request.POST["first_name"]
        username     = request.POST["username"]
        email        = request.POST["email"]
        pass1        = request.POST["pass1"]
        pass2        = request.POST["pass2"]
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken!")
                return redirect("register")
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is already taken!")    
                
            else:
                user= User.objects.create_user(first_name=first_name,username=username,email=email,password=pass1)
                user.save()
                return redirect("login")
        else:
            messages.info(request,"Password is not matching")
            return render(request,"register.html")
    return render(request,"register.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]
        
        user = auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return redirect("homePage")
        else:
            messages.info(request,"Invalid Credentials!")
            return redirect("login")    
    
    return render(request,"login.html")


def logout(request):
    
    auth.logout(request)
    return redirect("/")



