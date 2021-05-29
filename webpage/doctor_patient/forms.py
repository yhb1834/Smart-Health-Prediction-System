from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms.fields import EmailField
from django.forms.models import model_to_dict
from .models import Question, Pa_apllicationForm

# Admin 회원가입 폼
class AdUserForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ['username','email']

    def check_password(self):
        data = self.cleaned_data
        if data['password'] != data['check_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        return data['confirm_password']

# Admin 로그인 폼
class AdLoginForm(AuthenticationForm):
    email = forms.CharField(label='email',max_length=255)
    password = forms.CharField(label='password',widget=forms.PasswordInput)


# Patient 회원가입 폼
class PatientUserForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email']
    
    def check_password(self):
        data = self.cleaned_data
        if data['password'] != data['check_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        return data['confirm_password']

#Patient 로그인 폼
class PatientLoginForm(AuthenticationForm):
    email = forms.CharField(label='email',max_length=255)
    password = forms.CharField(label='password',widget=forms.PasswordInput)

#환자 신청 폼 
class PatientApplicationForm(forms.ModelForm):
    class Meta:
        model = Pa_apllicationForm
        fields = ['personalNuber','phoneNumber','address']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }


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

