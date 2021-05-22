from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class AdUserForm(UserCreationForm):
    class UserForm(UserCreationForm):
        email = forms.EmailField(label="이메일")

        class Meta:
            model = User
            fields = ("username", "email")

class PatientUserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")


#class LoginForm(AuthenticationForm):
    # 로그인 폼
    # email = forms.CharField(label='email',max_length=255)     
    #password = forms.CharField(label='password',widget=forms.PasswordInput)


#class QuestionForm(forms.ModelForm):
    # 질문 작성 폼
    #class Meta:
        #model = Question
        #fields = ['title', 'content']


#class AnswerForm(forms.ModelForm):
    # 답변 작성 폼
    #class Meta:
        #model = Answer
        #fields = ['content']



#class Reviewform(forms.ModelForm):
    #후기 폼
    #class Meta:
        #model = Review
        #fields = ['title', 'content']

