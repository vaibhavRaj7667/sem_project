from django.shortcuts import render,redirect
# from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate , login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import Student_user_creation_form
from django.contrib import messages
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required
from .models import questions
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import logout

# Create your views here.
# def home(request):
#     all_questions = questions.objects.all()
#     return render(request,'home.html',{'all_questions': all_questions})

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

def logout_view(request):
    logout(request)
    return redirect('login')


def home(request):
    all_questions = questions.objects.all()
    return render(request,'home.html',{'all_questions': all_questions})

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

@login_required
def delete_question(request, question_id):
    question = get_object_or_404(questions, id=question_id, user=request.user)
    if request.method == "POST":
        question.delete()
        return redirect('home')
        
    return render(request, 'delete_question.html', {'question': question})
        
    