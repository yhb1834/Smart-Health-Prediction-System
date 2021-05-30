from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import User, Question, Pa_apllicationForm

# UserCreationForm 상속 후 email attribute 추가
# username, password1, password, email 이라는 attribute들을 가지는 class.
class PatientForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("username", "email")
    
    def check_password(self):
        data = self.cleaned_data
        if data["password"] != data["check_password"]:
            raise forms.ValidationError("Password error.")
        return data["confirm_password"]

# still testing (이상진)

class PatientLoginForm(AuthenticationForm):
    email = forms.CharField(label='email',max_length=255)
    password = forms.CharField(label='password',widget=forms.PasswordInput)

class PatientApplicationForm(forms.ModelForm):
    class Meta:
        model = Pa_apllicationForm
        fields = ['symptom','doctor']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }