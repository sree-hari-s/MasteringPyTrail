from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import Tasks
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,'User Doesnot exist')
            return redirect('loginpage')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Credentials doesnot matched')
            return redirect('loginpage')
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email id already exists")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.infor(request,"Username alreadyy in use")
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, email = email, password=password)
                user.save()
                login(request,user)
                return redirect('loginpage')
        else:
            messages.error(request,"passwords are not matched!")
            return redirect('register')
    return render(request,'register.html')

@login_required(login_url='loginpage')
def home(request):
    tasks = Tasks.objects.all()
    content ={
        'tasks':tasks,
    }
    return render(request,'home.html',content)

@login_required(login_url='loginpage')
def addlist(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        username = request.POST.get('username')
        tasks = Tasks.objects.create(task = task,username =username)
        tasks.save()
        return redirect('home')

@login_required(login_url='loginpage')
def delete(request,pk):
    task = Tasks.objects.filter(id = pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request,'delete.html',{'obj':task})