from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label="email")
    #position = forms.CharField(label="position",default = "doctor",max_length =10)
    class Meta:
        model = User
        fields = ("username","email","password1","password2")
        

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'password']