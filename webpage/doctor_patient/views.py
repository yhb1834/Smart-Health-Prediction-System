from django.shortcuts import render

# Create your views here.
def ad_main(request):
    return render(request, 'ad/main.html')

def ad_login(request):
    return render(request, 'ad/login.html')

def ad_signup(request):
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
       return render(request, 'ad/signup.html', {'form': form})