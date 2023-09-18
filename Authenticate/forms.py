from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


#heredo de la clase UserCreationFomr
class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


    def __init__(self, *args, **kwargs):
        super(CreateNewUser, self).__init__(*args, **kwargs)

        #Personalizar mensajes del form
        self.fields["username"].error_messages.update({
            "required": "The username already exists" 
        })

        #agregar un atributo a cada input
        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Username",
            "id": "username"
            })
        
        self.fields["email"].widget.attrs.update({
            "class": "form-control", 
            "placeholder": "Email", 
            "id": "email"
            })
        
        self.fields["password1"].widget.attrs.update({
            "class": "form-control", 
            "placeholder": "Password", 
            "id": "password"
            })
        
        self.fields["password2"].widget.attrs.update({
            "class": "form-control", 
            "placeholder": "Repeat your password", 
            "id": "password2"
            })


#reset password
class ResetPassword(PasswordChangeForm):
    class Meta:
        model = PasswordChangeForm
        fields = ["new_password2"]
        