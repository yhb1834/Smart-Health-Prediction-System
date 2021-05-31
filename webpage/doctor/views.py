from django.shortcuts import render, redirect
from .models import Doctor_user, Earnings, Feedback, Prescription,Patient_list,Reservation
from .forms import UserForm,PrescriptionForm, FeedbackForm
#비밀번호 암호화 / 패스워드 체크(db에있는거와 일치성확인)
#make_password(str) : 이 함수에 넣어준 문자열을 암호화 (hashing)
#check_password(a,b) : a,b가 일치하는지 확인, 반환 
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import LoginForm

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from doctor_patient.settings import AUTH_USER_MODEL
from doctor_patient.models import User

from django.core.paginator import Paginator

#계정 생성 페이지(완료)
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
            res_data['error'] = '비밀번호가 다릅니다!'
        elif not (username and email and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다!'
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

#로그인 페이지(완료)
def doctor_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # session_code 검증하기
            request.session['user'] = form.user_id
            return redirect('../login-success')
    else:
        form = LoginForm()

    return render(request, 'doctor/login.html', {'form': form})

#로그인 성공(완료)
def doctor_login_success(request):
    user_id = request.session.get('user')
    
    if user_id:
        return render(request, 'doctor/login-success.html',{'login':1})

#로그아웃(완료)
def doctor_logout(request):
    user_id = request.session.get('user')
    
    if user_id:
        if request.session.get('user'):
            del(request.session['user'])
            return render(request, 'doctor/logout.html')
        

#메인 페이지(완료)
def doctor_main(request):
    user_id = request.session.get('user')
    
    if user_id:
        return render(request, 'doctor/main.html',{'login':1})
    return render(request, 'doctor/main.html')

#환자 리스트 보여주는 페이지(완료 ,유저 db 연결 필요)
def doctor_patient_list(request):
    user_id = request.session.get('user')
    
    if user_id:
        page = request.GET.get('page', '1')  # 페이지
        doctor_user = Doctor_user.objects.get(pk=user_id)
        patient_list = Patient_list.objects.select_related('doctor_name').filter(doctor_name__username = doctor_user.username)
        paginator = Paginator(patient_list, 8)  # 페이지당 10개씩 보여주기
        page_obj = paginator.get_page(page)
        
        
        return render(request, 'doctor/patient-list.html', {"question_list":page_obj,"doctor_name": doctor_user.username})
    
    return render(request, 'doctor/no-permission.html')
    
    
#처방전 작성 보여주는 페이지(완료 ,유저 db 연결 필요)
def doctor_prescription(request):
    user_id = request.session.get('user')
    
    if user_id:
        
        if request.method == "GET":
            doctor_user = Doctor_user.objects.get(pk=user_id)
            patient_name="김효진"
            symptom = str("머리가 아프고 열이 나요.")
            form = PrescriptionForm()
            return render(request, 'doctor/prescription.html',{"patient_name":patient_name,
                                                            "doctor_name": doctor_user.username,
                                                            "symptom" : symptom,
                                                            "form" : form
                                                            })
            
        elif request.method == "POST":
            form = PrescriptionForm(request.POST)
            doctor_user = Doctor_user.objects.get(pk=user_id)
            patient_name="김효진"
            symptom = str("머리가 아프고 열이 나요.")
            if form.is_valid():
                
                prescription = Prescription()
                prescription.doctor_name = doctor_user
                prescription.patient_name = patient_name
                prescription.symptom = symptom
                prescription.diagnosis = form.cleaned_data['diagnosis']
                prescription.save()
                return redirect('../patient-list')
            else:
                return render(request, 'doctor/prescription.html',{"patient_name":patient_name,
                                                            "doctor_name": doctor_user.username,
                                                            "symptom" : symptom,
                                                            "form" : form
                                                            })
    return render(request, 'doctor/no-permission.html')


#실시간 상담 및 예약 보여주는 페이지(완료 ,유저 db 연결 필요)
def doctor_reservation(request):
    user_id = request.session.get('user')
    
    if user_id:
        doctor_user = Doctor_user.objects.get(pk=user_id)
        if request.method == "GET":#페이지 보여주는 곳
            return render(request, 'doctor/reservation.html',{
                                                            "doctor_name": doctor_user.username,
                                                            "login":1,
                                                            })
        
        elif request.method == "POST":
            date = request.POST.get('date', None)
            time = request.POST.get('time', None)
            patient_name = request.POST.get('patient_name', None)
            type = request.POST.get('type', None)
            content = request.POST.get('content', None)
            res_data = {}
            if not (type and time and content and patient_name and date):
                res_data['error'] = '아직 작성하지 않은 부분이 있습니다!'
            else:
                patient_name = User.objects.get(username=patient_name)
                reservation = Reservation(
                    doctor_name = doctor_user,
                    date=date,
                    patient_name=patient_name,
                    type=type,
                    content=content,
                    time=time
                )
                reservation.save()
                return redirect('../../doctor/main')
            res_data['doctor_name'] = doctor_user.username
            res_data['login'] = 1
            return render(request, 'doctor/reservation.html',res_data)
    
    return render(request, 'doctor/no-permission.html')

#피드백 페이지(완료 ,유저 db 연결 필요)
def doctor_feedback(request):
    user_id = request.session.get('user')
    
    if user_id:
        if request.method == "GET":
            doctor_user = Doctor_user.objects.get(pk=user_id)
            form = FeedbackForm()
            return render(request, 
                        'doctor/feedback.html',
                        {"doctor_name": doctor_user.username,
                        "form" : form})
            
        elif request.method == "POST":
            form = FeedbackForm(request.POST)
            doctor_user = Doctor_user.objects.get(pk=user_id)
            if form.is_valid():
                
                feedback = Feedback()
                feedback.username = doctor_user
                feedback.content = form.cleaned_data['content']
                feedback.title = form.cleaned_data['title']
                feedback.position = "doctor"
                feedback.save()
                return redirect('../patient-list')
            else:
                return render(request, 
                        'doctor/feedback.html',
                        {"doctor_name": doctor_user.username,
                        "form" : form})  
    return render(request, 'doctor/no-permission.html')

    
#돈 받는 페이지(완료 ,유저 db 연결 필요)
def doctor_earnings(request):
    user_id = request.session.get('user')
    
    if user_id:
        doctor_user = Doctor_user.objects.get(pk=user_id)
        if request.method == "GET":
            return render(request, 'doctor/earnings.html',{
                                                            "doctor_name": doctor_user.username,
                                                            "total_money":doctor_user.money,
                                                            "login":1,
                                                            })
            
        elif request.method == "POST":    
            bank = request.POST.get('bank', None)
            account = request.POST.get('account', None)
            money = request.POST.get('money', None)
            res_data = {}
            if not (bank and account and money):
                res_data['error'] = '아직 작성하지 않은 부분이 있습니다!'
            if money > doctor_user.money:
                res_data['error'] = 'Total Coin보다 더 많은 Coin 수를 입력할 수 없습니다!'
            else:
                earnings = Earnings(
                    doctor_name = doctor_user,
                    money = money,
                    account = account,
                    bank = bank
                )
                doctor_user.money = doctor_user.money - money
                doctor_user.save()
                earnings.save()
                return redirect('../../doctor/main')
            res_data['doctor_name'] = doctor_user.username
            res_data['total_money'] = doctor_user.money
            res_data['login'] = 1
            return render(request, 'doctor/earnings.html',res_data)

            
    return render(request, 'doctor/no-permission.html')
