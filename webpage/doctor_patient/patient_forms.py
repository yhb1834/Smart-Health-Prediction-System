from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

# UserCreationForm 상속 후 email attribute 추가
# username, password1, password, email 이라는 attribute들을 가지는 class.
class PatientForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("username", "email")

# still testing (이상진)
