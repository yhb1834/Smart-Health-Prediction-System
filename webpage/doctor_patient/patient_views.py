from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import RemoteUserBackend
from django.shortcuts import render, redirect
from .forms import PatientUserForm, PatientLoginForm
from django.contrib.auth.models import Group, User

def pa_main(request):
    return render(request,'patient/main.html')

def pa_login(request):
    if request.method == 'POST':
        form = PatientLoginForm(request, request.POSST)
        if form.is_valid():
            login(request, form.get_user(), backend='django.contrib.auth.backends.ModelBackend')
            return redirect('../main')
        else:
            return render(request,"patient/login.html", {'form': form,"message": "Please check your email and password again"})
    else:
        form = PatientLoginForm()
    return render(request, 'patient/login.html')

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

def pa_feedback(request):
    #나중에 피드백 저장 모델 하고 폼 만들기
    return render(request, 'patient/feedback.html')