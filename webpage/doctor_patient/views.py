from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from doctor_patient.forms import AdUserForm, AdLoginForm, DoctorUserForm, QuestionForm # 여기 부분에 forms.py에 넣어져 있는 것들 꼭 추가!!!
from django.utils import timezone
from .models import User
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


# admin 로그아웃
def admin_logout(request):
    user_id = request.session.get('user')

    if user_id:
        if request.session.get('user'):
            del (request.session['user'])
            return render(request, 'ad/logout.html')

# admin 회원가입 페이지
def ad_signup(request):
    #계정 생성
       if request.method == "POST":
           form = AdUserForm(request.POST)
           if form.is_valid():
               form.save()
               '''
               어떻게 하면 값을 ture 할 수있는지 연습 인데 안되네 ㅠㅠㅠㅠ
               user_id = request.session.get('username')
               userobj = User.objects.get(username=user_id)
               if not userobj.is_admin:
                   userobj.is_admin = False 
                '''
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
            feedback = form.save(commit=False)
            feedback.create_date = timezone.now()
            feedback.save()
            return redirect('../feedback')
    else:
        form = QuestionForm()
    context = {"form": form}
    return render(request, 'ad/feedbackwrite.html', context)


# 임시로 doctor_관련 view들 추가하여 작업중 (이상진)
# doctor subgroup의 임의 수정가능.
def doctor_main(request):
    return render(request, 'doctor/main.html')

def doctor_login(request):
    return render(request, 'doctor/login.html')

def doctor_signup(request):
    #계정 생성
       if request.method == "POST":
           form = DoctorUserForm(request.POST)
           if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               raw_password = form.cleaned_data.get('password1')
               user = authenticate(username=username, password=raw_password)
               login(request, user)
               return redirect('index')
       else:
           form = DoctorUserForm()
       return render(request, 'doctor/signup.html', {'form': form})

def doctor_feedback(request):
    return render(request, 'doctor/feedback.html')

def doctor_patient_list(request):
    return render(request, 'doctor/patient-list.html')

def doctor_prescription(request):
    return render(request, 'doctor/prescription.html')

def doctor_reservation(request):
    return render(request, 'doctor/reservation.html')