from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth  import  authenticate,login,logout
from django.contrib.auth.models  import User,auth
# Create your views here.
from supply.models import Water
from django.contrib.auth.forms import UserCreationForm



def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,"index.html",{})
        else:
            return render(request,"signupp.html")
    else:
        return render(request,"loginn.html")
        # takes you to sign in form.
    #if request.method== 'POST':
     #   username = request.POST['username']
      #  password = request.POST['password']
       # user = authenticate(request,username=username,password=password)
        
        #if user:
         #   login(request, user)
          #  return redirect("supply")
        #else:
         #   messages.info(request,'invalid credentials')
          #  return redirect('loginn')

   # else:
    #    return render(request,'loginn.html')    

def signupp(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('signupp')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('signupp')
            else:   
                #user = User.objects.create(username=username, password=password, email=email)
                #user.save()
                user = User.objects.create_user(username=username,password=password,email=email)
                user.password = password
                user.set_password(user.password)
                user.is_staff=True
                user.is_superuser=True
                user.save()
                print('user created')
                return redirect('loginn')

        else:
            messages.info(request,'password not matching..')    
            return redirect('signupp')
        return redirect('/')
        
    else:
        return render(request,'signupp.html')



def supply(request):
        return render(request,'index.html')  
        

def vendor(request):
        return render(request,'vendor.html')

def placetheorder(request):
        
        return render(request,'placetheorder.html')  

def about(request):
        return render(request,'about.html')  
def legal(request):
        return render(request,'legal.html')
def contact(request):
        return render(request,'contact.html')

def logout(request):
        auth.logout(request)
        return render(request,'index.html')

def thank(request):
        return render(request,'thankyou.html')
def location(request):
        return render(request,'location.html')