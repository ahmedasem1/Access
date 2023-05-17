from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def SignupPage(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        x = str(User.objects.filter(username=uname))
        if "@" in x:
            messages.error(request, "username exsists")
            return redirect("signup")

        emp = request.POST.get("emp")

        password = request.POST.get("password1")
        confirm = request.POST.get("password2")
        if password != confirm:
            messages.error(request, "Your password and confrom password are not Same!!")
            return redirect("signup")

        else:
            my_user = User.objects.create_user(
                username=uname, email=uname, first_name=emp, password=password
            )
            my_user.save()
            login(request, my_user)

            if emp == "emp":
                return redirect("signupemp")
            else:
                return redirect("signupcomp")

    return render(request, "authentication/signup.html")


def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass")

        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect("jobs")
        else:
            messages.error(request, "Username or Password is incorrect!!!")
            return redirect("login")

    return render(request, "authentication/login.html")


def LogoutPage(request):
    logout(request)
    return redirect("login")
