from django.shortcuts import render
from Authenticate.forms import CreateNewUser


# Create your views here.
def index(request):

    form = CreateNewUser()

    if request.method == "POST":
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
        
    return render(request, "index.html", {"form":form})