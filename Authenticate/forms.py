from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


#heredo de la clase UserCreationFomr
class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

