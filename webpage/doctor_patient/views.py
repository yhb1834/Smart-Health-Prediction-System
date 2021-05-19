from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'doctor_patient/main.html')

def login(request):
    return render(request, 'doctor_patient/login.html')

def signup(request):
    return render(request, 'doctor_patient/signup.html')