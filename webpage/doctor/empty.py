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