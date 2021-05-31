from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import RemoteUserBackend
from django.shortcuts import render, redirect
from .forms import PatientUserForm, PatientLoginForm, PatientApplicationForm, PatientDetailsForm, PatientReportForm, QuestionForm
from django.utils import timezone
from .models import User, Pa_details, Pa_report
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from doctor.models import Doctor_user

def pa_main(request):
    context = {
        'patient_name': request.user.username,
    }
    return render(request,'patient/main.html', context)

def pa_search(request):
    #home이라 생각하고 여기에 검색 기능이 있어야 하지 않을까? 아니면 나중에 main 하고 합치던지
    #일단 main.html로 연결해 놓는데  나중에 검색결과 페이지를 따로 만들어서 그 검색결과 페이지를 렌더 해야 합니다

    #이게 검색 기능 나중에 html에 연결
    q = request.GET.get('q')

    if q:
        #일단 q로 가져오는 것 까지는 성공
        doctor_list=Doctor_user.objects.all().order_by('username')
        search = doctor_list.filter(username__icontains=q)
        print(len(search))
        for i in search:
            print(i)
        context ={
            'doctors':search,
        }
        #검색된 사람들의 정보를 넘겨줌
        return render(request, 'patient/searchlist.html', context)

    return render(request,'patient/search.html')

#이거 프론트하고 연결 해야 합니다.
def pa_login(request):
    if request.method == 'POST':
        form = PatientLoginForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user(), backend='django.contrib.auth.backends.ModelBackend')
            return redirect('../main')
        else:
            return render(request,"patient/login.html", {'form': form,"message": "Please check your email and password again"})
    else:
        form = PatientLoginForm()
    return render(request, 'patient/login.html', {'form': form})

def pa_logout(request):
    #로그아웃
    logout(request)
    return redirect('../main')

def pa_signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = PatientUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            #이거 리다이렉트 어떻게 보내는 거??? 모르겠음
            return redirect('../login')
    else:
        form = PatientUserForm()
    return render(request, 'patient/signup.html', {'form': form})


#어플리케이션 폼 나중에 html하고 연결 
def pa_application(request):
    if not request.user.is_authenticated:
        return redirect('../login')

    if request.method == 'POST':
        form = PatientApplicationForm(request.POST)
        if form.is_valid():
            appl = form.save(commit=False)
            appl.create_date = timezone.now()
            appl.save()

    form = PatientApplicationForm()
    context = {
        'form' : form,
    }
    return render(request, 'patient/application.html', context)

def pa_feedback(request):
    
    if not request.user.is_authenticated:
        return redirect('../login')

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.create_date = timezone.now()
            feed.save()

    form = QuestionForm()
    context = {
        'patient_name': request.user.username,
        'form' : form,
    }
    
    return render(request, 'patient/feedback.html', context)

#아직 작업중인 부분 
def pa_details(request):
    #환자 세부 정보를 작성 및 보이기.
    
    if not request.user.is_authenticated:
        return redirect('../login')
    '''
    if request.method == 'POST':
        form = PatientDetailsForm(request.POST)
        if form.is_valid():
            form.save()

    _user_id = request.session.get('user') 
    obj = Pa_details.objects.get(user = _user_id)

    if obj:
        # 작성된 것 있다면, 보여주기
        context = {
            'form' : form,
            'patient_name' : obj.age,
            'PID' : obj.personalID,
            'patient_email' : obj.email,
            'age' : obj.age,
            'sex' : obj.sex,
            'u_disease' : obj.underlying_disease,
            'phone_num' : obj.phone_num,
            'address' : obj.address
        }
    else:
        # 작성하기
        form = PatientDetailsForm()
    '''
    context = {
        'form' : "form",
        'patient_name' : "obj.age",
        'PID' : "obj.personalID",
        'patient_email' : "obj.email",
        'age' : "obj.age",
        'sex' : "obj.sex",
        'u_disease' : "obj.underlying_disease",
        'phone_num' : "obj.phone_num",
        'address' : "obj.address"
    }

    return render(request, 'patient/details.html', context)

def pa_report(request):
    #환자 증상을 기술하는 부분
    if not request.user.is_authenticated:
        return redirect('../login')
    if request.method == 'POST':
        form = PatientReportForm(request.POST)
        if form.is_valid():
            form.save()

    form = PatientReportForm()
    context = {
        'form' : form,
    }

    return render(request, 'patient/report.html', context)

def pa_prescription(request, id):
    #환자가 작성한 reportfrom을 보여주는 부분
    prediscription = Pa_report.objects.all(userid = id)
    form = prediscription
    context = {
        'form' : form,
    }
    return render(request, 'patient/prescription.html', context)
