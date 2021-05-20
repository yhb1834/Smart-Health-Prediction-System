from django.shortcuts import render

def pa_main(request):
    return render(request,'patient/main.html')

def pa_login(request):
    return render(request, 'patient/login.html')

def pa_signup(request):
    

    return render(request, 'patient/signup.html')