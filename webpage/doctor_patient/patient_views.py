from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import RemoteUserBackend
from django.shortcuts import render, redirect
from .forms import PatientUserForm, PatientLoginForm, Pa_apllicationForm
from django.utils import timezone
from django.contrib.auth.models import Group, User

def pa_main(request):
    return render(request,'patient/main.html')

def home(request):
    #home이라 생각하고 여기에 검색 기능이 있어야 하지 않을까? 아니면 나중에 main 하고 합치던지
    #일단 main.html로 연결해 놓는데  나중에 검색결과 페이지를 따로 만들어서 그 검색결과 페이지를 렌더 해야 합니다

    #이게 검색 기능 나중에 html에 연결
    q = request.POST.get('q', "")
    if q:
        doctor_list=User.objects.all().order_by('username')
        search = doctor_list.filter(UsernameField=q)
        context ={
            'doctors':search,
        }
        #검색된 사람들의 정보를 넘겨줌
        return render(request, 'patient/main.html', context)

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


#어플리케이션 폼 나중에 html하고 연결 
def pa_application(request):
    if not request.user.is_authenticated:
        return redirect('../login')
    
    if request.method == 'POST':
        form = Pa_apllicationForm(request.POST)
        if form.is_valid():
            appl = form.save(commit=False)
            appl.create_date = timezone.now()
            appl.save()
    
    form = Pa_apllicationForm()
    context = {
        'form' : form,
    }
    return render(request, 'patient/application.html')

def pa_feedback(request):
    #나중에 피드백 저장 모델 하고 폼 만들기
    return render(request, 'patient/feedback.html')