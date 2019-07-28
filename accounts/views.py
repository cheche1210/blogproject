from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':#request.method로 하면 에러가 뜬다 
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
            auth.login(request,user)
            return redirect('home')#blog에 대한 url로 이동
    return render(request,'signup.html')#아니면 계속 머물러

def login(request):
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error':'아이디 혹은 비밀번호가 틀립니다'})
    else:
         return render(request,'login.html')

def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return redirect('home')
    else:
        print(request.method)
        return render(request, 'login.html')
  
        