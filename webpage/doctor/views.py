from django.shortcuts import render, redirect
from .models import Doctor_user#의사 모델.py
from .models import Patient_list
#응답에 대한 메타정보를 포함한 객체
#로그인 완료시에 "로그인 완료" 라는 text를 띄우기 위해 임포트
from django.http import HttpResponse
from django.contrib.auth import logout
#비밀번호 암호화 / 패스워드 체크(db에있는거와 일치성확인)
#make_password(str) : 이 함수에 넣어준 문자열을 암호화 (hashing)
#check_password(a,b) : a,b가 일치하는지 확인, 반환 
from django.contrib.auth.hashers import make_password, check_password

from .forms import UserForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.http import HttpResponse


#계정 생성 페이지
def doctor_signup(request):
    if request.method == "GET":
        return render(request, 'doctor/signup.html')
    elif request.method == "POST":
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password1', None)
        re_password = request.POST.get('password2', None)
        res_data = {}
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        elif not (username and email and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다'
        else:
            doctor_user = Doctor_user(
                username=username,
                password=make_password(password),
                email=email,
            )
            doctor_user.save()
            return redirect('../../doctor/main')
        
        return render(request, 'doctor/signup.html',res_data)
    return render(request, 'doctor/signup.html')


# def doctor_signup(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('doctor/main.html')
#     else:
#         form = UserForm()
#     return render(request, 'doctor/signup.html',{'form': form})

#로그인 페이지
def doctor_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # session_code 검증하기
            request.session['user'] = form.user_id
            return redirect('../../doctor/patient-list')
    else:
        form = LoginForm()

    return render(request, 'doctor/login.html', {'form': form})
'''
def doctor_login(request):
    if request.method == "GET":
        return render(request, 'doctor/login.html')
    elif request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        
        res_data = {}
        if not (email and password):
            res_data['error'] = '모든 값을 입력하세요!'
            
        else:
            doctor_user = Doctor_user.objects.get(email = email)
            
            if check_password(password, doctor_user.password):
                request.session['user'] = doctor_user.id
                return redirect('../../doctor/patient-list')
        
            else:# 비밀번호가 다른 경우
                res_data['error'] = 'Please enter a valid email or password'
        
        return render(request, 'doctor/login.html', res_data)         
    '''
    
    
            
# def doctor_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(email = email, password = password)
#         if user is not None:
#             login(request, user)
#             return redirect('doctor/main.html')
#         else:
#             return HttpResponse('Login failed. Try again.')
#     else:
#         form = LoginForm()
#         return render(request, 'doctor/login.html')

#로그아웃
def doctor_logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('../../doctor/main')

#메인 페이지
def doctor_main(request):
    return render(request, 'doctor/main.html')


#환자 리스트 보여주는 페이지
def doctor_patient_list(request):
    user_id = request.session.get('user')
    
    if user_id:
        doctor_user = Doctor_user.objects.get(pk=user_id)
        patient_list = Patient_list.objects.select_related('doctor_name').filter(doctor_name__username = doctor_user.username)
        return render(request, 'doctor/patient-list.html', {"patient_list":patient_list,"doctor_name": doctor_user.username})
    
    return HttpResponse('Home!')
    

#처방전 작성 보여주는 페이지
def doctor_prescription(request):
    return render(request, 'doctor/prescription.html')

#실시간 상담 및 예약 보여주는 페이지
def doctor_reservation(request):
    return render(request, 'doctor/reservation.html')

#돈 받는 페이지
def doctor_medical_expense(request):
    #return render(request, 'doctor/-list.html')
    pass

#피드백
def doctor_feedback(request):
    return render(request, 'doctor/feedback.html')
    pass