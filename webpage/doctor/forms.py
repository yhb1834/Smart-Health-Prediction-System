from doctor.models import Doctor_user
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class UserForm(UserCreationForm):
    email = forms.EmailField(label="email")
    #position = forms.CharField(label="position",default = "doctor",max_length =10)
    class Meta:
        model = User
        fields = ("username","email","password1","password2")
        

class LoginForm(forms.Form):
    # 입력받을 값 두개
    email = forms.CharField(error_messages={
        'required':'이메일을 입력하세요!'
    },max_length=100,widget=forms.EmailInput, label="Email address")
    password = forms.CharField(error_messages={
        'required':'비밀번호를 입력하세요!'
    },widget=forms.PasswordInput, max_length=100, label="Password")
    # 처음 값이 들어왔다 는 검증 진행
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            member = Doctor_user.objects.get(email=email)

            if not check_password(password, member.password):
                self.add_error('password', '비밀번호가 다릅니다!')
            else:
                self.user_id = member.id

