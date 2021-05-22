from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import PatientUserForm

def pa_main(request):
    return render(request,'patient/main.html')

def pa_login(request):
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
            return redirect('pa_main')
    else:
        form = PatientUserForm()
    return render(request, 'patient/signup.html', {'form': form})
