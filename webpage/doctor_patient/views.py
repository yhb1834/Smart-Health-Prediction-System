from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from doctor_patient.forms import AdUserForm, AdLoginForm, DoctorUserForm, QuestionForm # 여기 부분에 forms.py에 넣어져 있는 것들 꼭 추가!!!
from django.utils import timezone

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from doctor.models import Feedback

# Create your views here.

# 랜딩페이지
def home(request):
    return render(request, 'home.html')

# admin main 페이지
def ad_main(request):
    return render(request, 'ad/main.html')

# admin 로그인 페이지
def ad_login(request):
    if request.method =='POST':
        user_form = AdLoginForm(request,request.POST)
        if user_form.is_valid():
            login(request, user_form.get_user(), backend='django.contrib.auth.backends.ModelBackend')
            return redirect('../main')
        else:
           return render(request,"ad/login.html", {'form': user_form,"message": "Please check your email and password again"})
    else:
        user_form = AdLoginForm()
    return render(request, 'ad/login.html',{'form': user_form})

# admin 회원가입 페이지
def ad_signup(request):
    #계정 생성
       if request.method == "POST":
           form = AdUserForm(request.POST)
           if form.is_valid():
               #form.setAdmin() is_admin 값 어떻게 바꾸냐???? 일단 이건 안되는데
               form.save()
               username = form.cleaned_data.get('username')
               raw_password = form.cleaned_data.get('password1')
               user = authenticate(username=username, password=raw_password)
               login(request, user)
               return redirect('../main')
       else:
           form = AdUserForm()
       return render(request, 'ad/signup.html', {'form': form})

# admin 의사 자격 확인 페이지
def ad_doctor_certify(request):
    return render(request, 'ad/doctorcertify.html')

# admin feedback 리스트 페이지
def ad_feedback(request):
    feedback_list = Feedback.objects.all()
    return render(request, 'ad/feedback.html',{"feedback_list":feedback_list})

# admin feedback 쓰기 페이지
def ad_feedback_write(request):

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            feedback = Feedback()
            feedback.username = "admin"
            feedback.content = form.cleaned_data['content']
            feedback.title = form.cleaned_data['title']
            feedback.position = "admin"
            feedback.save()
            
            #feedback = form.save(commit=False)
            #feedback.create_date = timezone.now()
            #feedback.save()
            return redirect('../feedback')
    else:
        form = QuestionForm()
    context = {"form": form}
    return render(request, 'ad/feedbackwrite.html', context)



