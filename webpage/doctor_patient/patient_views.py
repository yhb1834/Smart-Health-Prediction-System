from django.shortcuts import render

def pa_main(request):
    return render(request,'patient/main.html')

def pa_login(request):
    # validation check 필요?:w
    return render(request, 'patient/login.html')

def pa_signup(request):
    # 회원가입.
    
    return render(request, 'patient/signup.html')