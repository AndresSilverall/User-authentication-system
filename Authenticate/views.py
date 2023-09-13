from django.shortcuts import render
from Authenticate.forms import CreateNewUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm #Me trae los campos Username, password, repeat password


# Create your views here.
def home(request):
    return render(request, "home.html")



def index(request):

    form = CreateNewUser()

    if request.method == "POST":
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
        
    return render(request, "index.html", {"form":form})