from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from doctor_patient.forms import AdUserForm, AdLoginForm # 여기 부분에 forms.py에 넣어져 있는 것들 꼭 추가!!!

# Create your views here.
def ad_main(request):
    return render(request, 'ad/main.html')

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

def ad_signup(request):
    #계정 생성
       if request.method == "POST":
           form = AdUserForm(request.POST)
           if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               raw_password = form.cleaned_data.get('password1')
               user = authenticate(username=username, password=raw_password)
               login(request, user)
               return redirect('../main')
       else:
           form = AdUserForm()
       return render(request, 'ad/signup.html', {'form': form})

def ad_doctor_certify(request):
    return render(request, 'ad/doctorcertify.html')

def ad_feedback(request):
    return render(request, 'ad/feedback.html')

def ad_feedback_write(request):
    return render(request, 'ad/feedbackwrite.html')


# 임시로 doctor_관련 view들 추가하여 작업중 (이상진)
# doctor subgroup의 임의 수정가능.
def doctor_main(request):
    return render(request, 'doctor/main.html')

def doctor_login(request):
    return render(request, 'doctor/login.html')

def doctor_signup(request):
    #계정 생성
       if request.method == "POST":
           form = UserForm(request.POST)
           if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               raw_password = form.cleaned_data.get('password1')
               user = authenticate(username=username, password=raw_password)
               login(request, user)
               return redirect('index')
       else:
           form = UserForm()
       return render(request, 'doctor/signup.html', {'form': form})