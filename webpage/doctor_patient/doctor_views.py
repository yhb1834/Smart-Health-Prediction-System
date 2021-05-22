from django.shortcuts import render, redirect

from .doctor_models import Doctor_user#의사 모델.py

#응답에 대한 메타정보를 포함한 객체
#로그인 완료시에 "로그인 완료" 라는 text를 띄우기 위해 임포트
from django.http import HttpResponse

#비밀번호 암호화 / 패스워드 체크(db에있는거와 일치성확인)
#make_password(str) : 이 함수에 넣어준 문자열을 암호화 (hashing)
#check_password(a,b) : a,b가 일치하는지 확인, 반환 
from django.contrib.auth.hashers import make_password, check_password 


#메인 페이지
def doctor_main(request):
    return render(request, 'doctor/main.html')

#로그인 페이지
def doctor_login(request):
    response_data = {}

    if request.method == "GET":
        return render(request, 'doctor/login.html')
    
    elif request.method == "POST":
        login_username = request.POST.get('username', None)
        login_password = request.POST.get('password', None)

        # if not (login_username and login_password):
        #     response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
        # else : 
        #     #POST로 들어온 login_username으로 Myuser클래스에서 데이터를 꺼내옵니다. (username, password, email)
        #     myuser = Myuser.objects.get(username=login_username) 
        #     #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
        #     if check_password(login_password, myuser.password):
        #         #세션(session)에 id값을 넣습니다. 로그인 상태를 유지하기 위함입니다.
        #         request.session['user'] = myuser.id 
        #         #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
        #         #세션 user라는 key에 방금 로그인한 id를 저장한것.
        #         return redirect('/')
        #     else:
        #         response_data['error'] = "비밀번호를 틀렸습니다."

        return render(request, 'login.html',response_data)


#계정 생성 페이지
def doctor_signup(request):
    #계정 생성
    if request.method == "GET":
        return render(request,'doctor/signup.html')

    elif request.method == "POST":
        username = request.POST.get('username') #딕셔너리형태
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        res_data = {} 
        if not (username and password and re_password) :#모든 정보를 입력하지 않았을 경우
            res_data['error'] = "You have to enter all the information."
        if password != re_password :
            #res_data : 위 html 파일에서 {{error}}와 맵핑되어 처리됩니다. 
            #즉, if문에서 걸리면 뒤의 문자열이 출력됩니다.
            # return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = 'password is differnet'
        else :
            doctor_user = Doctor_user(username=username, password=make_password(password))
            doctor_user.save()
        return render(request, 'doctor/signup.html', res_data) #register를 요청받으면 register.html 로 응답.

    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         raw_password = form.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=raw_password)
    #         login(request, user)
    #         return redirect('index')
    # else:
    #     form = UserForm()
    # return render(request, 'doctor/signup.html', {'form': form})

