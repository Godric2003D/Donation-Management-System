from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def all_logins(request):
    return render(request, 'all_logins.html')

def donor_login(request):
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username = u, password = p)
        if user:
            login(request,user)
            error = "no"
        else:
            error = "yes"
    return render(request, 'donor_login.html', locals())

def charfo_login(request):
    return render(request, 'charfo_login.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def donor_reg(request):
    error = ""
    if request.method == "POST":
        fn =request.POST['firstname']
        ln =request.POST['lastname']
        em =request.POST['email']
        contact =request.POST['contact']
        pwd =request.POST['pwd']
        userpic =request.FILES['userpic']
        address =request.POST['address']
        
        
        try:
            user = User.objects.create_user(first_name = fn,last_name=ln,username=em,password=pwd )
            Donor.objects.create(user=user, contact=contact,userpic=userpic,address=address)
            error="no"
        except:
            error="yes"
    return render(request, 'donor_reg.html',locals())

def charfo_reg(request):
    error = ""
    if request.method == "POST":
        fn =request.POST['firstname']
        ln =request.POST['lastname']
        em =request.POST['email']
        contact =request.POST['contact']
        pwd =request.POST['pwd']
        userpic =request.FILES['userpic']
        idpic =request.FILES['idpic']
        address =request.POST['address']
        
        
        try:
            user = User.objects.create_user(first_name = fn,last_name=ln,username=em,password=pwd )
            CharFound.objects.create(user=user, contact=contact,userpic=userpic,idpic=idpic,address=address)
            error="no"
        except:
            error="yes"
    return render(request, 'charfo_reg.html', locals())

def donor_home(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    return render(request, 'donor_home.html')

def donate_now(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    
    return render(request, 'donate_now.html')


def Logout(request):
    logout(request)
    return redirect('index')





    