from django.shortcuts import render, redirect
from Authenticate.forms import CreateNewUser
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm #Me trae los campos Username, password, repeat password


# Create your views here.
def home(request):
    return render(request, "navbar.html")


def logged_user(request):
    return render(request, "user_logged.html")


def register_user(request):
    form = CreateNewUser()

    if request.method == "POST":
        form = CreateNewUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            messages.success(request, f"User '{username}' created Successfully!")

    context = {
        "form": form
    } 

    return render(request, "register.html", context)


def login_user(request):
    form = CreateNewUser() 

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("logged")
        
    context = {
        "form": form
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    return render(request, "navbar.html")


def restart_password(request):
    pass