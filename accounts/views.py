from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages



def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password1= request.POST['password']
        password2= request.POST['password1']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                messages.info(request,'user created')
                return redirect('login')
        else:
            messages.info(request,'password not matching')
        return redirect('/')
    else:
        return render(request,'register.html')


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            msgs= 'successfully logged in'
            messages.info(request, msgs)
            return redirect('/')
        else:
            messages.info(request,'wrong credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

#to logout
def logout(request):
    auth.logout(request)
    return redirect('/')
