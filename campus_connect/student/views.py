from django.shortcuts import render,redirect
# from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate , login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import Student_user_creation_form
from django.contrib import messages
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            messages.info(request,("there was an error ocur"))
            return redirect('login')
    else:
        return render(request,'login_page.html')

def register(request):
    if request.method=='POST':
        form = Student_user_creation_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = Student_user_creation_form()
    return render(request,'register_user.html',{'form':form})

@login_required
def profile(request):
    if request.method=='POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()

    return render(request,'profile.html',{'form':form})