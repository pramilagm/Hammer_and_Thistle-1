from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from apps.home_app.models import *
from apps.login_app.models import *
import bcrypt

def login_splash(request): 
    return render(request,'login_app/login.html')

def register(request):
    error = User.objects.basic_validator(request.POST)

    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect('/login')
    else:
        request.session.clear()
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        pw_confirm = request.POST["pw_confirm"]
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(first_name = first_name, last_name = last_name, email = email, password = hashed_pw)

        logged_user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = logged_user.id
        request.session['first_name'] = first_name
        request.session['logged_in'] = True
        return redirect('/cart')

def login(request):
    request.session.clear()
    user = User.objects.filter(email=request.POST['email']) 
    if user:
        logged_user = user[0]

        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            request.session['logged_in'] = True
            request.session['first_name'] = logged_user.first_name
            return redirect('/cart')
        else:
                messages.error(request, "Password is not correct")
                return redirect("/login")

    messages.error(request, "The email was not found")
    return redirect("/")

def logout(request): 
    if 'logged_in' in request.session:
        request.session.clear()
    return redirect('/')
