from django.shortcuts import render,redirect
from django.contrib import messages
from showroom.models import Report,showroom,Shop
from datetime import datetime
from django.contrib.auth.models import User,auth
# Create your views here.

def cars(request):
    cars = showroom.objects.all()
    return render(request,'cars.html',{'cars':cars})


def contact(request):
    if request.method == "POST":
        name_us = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc_us = request.POST.get('desc')
        report = Report(name_us=name_us,email=email,phone=phone,desc_us=desc_us,date= datetime.today())
        report.save()
        messages.success(request, 'Your message has been sent')
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.success(request, 'Invalid credentials')
            return redirect("login")
    else:
        return render(request,"login.html")
def register(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.success(request, 'Username is already taken')
            elif User.objects.filter(email=email).exists():
                messages.success(request, 'Email is already taken')
            else:
                user = User.objects.create_user(first_name=name,email=email,username=username,password=password1)
                user.save()
                messages.success(request, 'Registration done')
                return redirect("login")
        else:   
            messages.success(request, 'Password and confirm password is not matching')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

def search(request):
    query = request.GET['query']
    all = showroom.objects.filter(name__icontains=query)
    params = {'all':all}
    return render(request,"search.html",params)

def shop(request):
    cars = showroom.objects.all()
    if request.method == "POST":
        desc = request.POST.get('desc')
        paymentMethod = request.POST.get('paymentMethod')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        shop = Shop(paymentMethod=paymentMethod,name=name,email=email,phone=phone,desc=desc,date= datetime.today())
        shop.save()
        messages.success(request, 'Your dream car will soon arrive.')
        return redirect("/")
    return render(request,"shop.html",{'cars':cars})
    