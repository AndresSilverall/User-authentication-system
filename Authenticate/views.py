from django.shortcuts import render
from Authenticate.forms import CreateNewUser
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm #Me trae los campos Username, password, repeat password


# Create your views here.
def home(request):
    return render(request, "home.html")


def login_user(request):
    return render(request, "login.html")


def register_user(request):

    form = CreateNewUser()

    if request.method == "POST":
        form = CreateNewUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            messages.success(request, f"User {username} created Succesfully!")

        else:
            form = CreateNewUser()
        
    return render(request, "index.html", {"form":form})