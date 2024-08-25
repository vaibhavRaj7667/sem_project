from django.shortcuts import render,redirect,HttpResponse
# from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate , login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import Student_user_creation_form
from django.contrib import messages
from .forms import QuestionForm,reply
from django.contrib.auth.decorators import login_required
from .models import questions
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import logout
from .forms import ReplyForm
from django.db.models import Q

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

@login_required
def home(request):
    all_questions = questions.objects.all().order_by('-created_on')
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
    user_question = questions.objects.filter(user=request.user).order_by('-created_on')
    if request.method=='POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()

    return render(request,'profile.html',{'form':form, 'user_question': user_question})

@login_required
def delete_question(request, question_id):
    question = get_object_or_404(questions, id=question_id, user=request.user)
    if request.method == "POST":
        question.delete()
        return redirect('home')
        
    return render(request, 'delete_question.html', {'question': question})
        

@login_required
def question_detail(request, question_id):
    question = get_object_or_404(questions, id=question_id)
    replies = question.replies.all()  # Fetch all replies related to this question

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            new_reply = form.save(commit=False)
            new_reply.user = request.user
            new_reply.question = question
            new_reply.save()
            return redirect('question_detail', question_id=question.id)
    else:
        form = ReplyForm()

    return render(request, 'question_detail.html', {
        'question': question,
        'replies': replies,
        'form': form
    })

# @login_required
# def delete_reply(request, reply_id):
#     reply = get_object_or_404(reply, id=reply_id, user=request.user)
#     if request.method == "POST":
#         reply.delete()
#         return redirect('question_detail', question_id=reply.question.id)
#     return redirect('question_detail', question_id=reply.question.id)

@login_required
def delete_reply(request, reply_id):
    reply_obj = get_object_or_404(reply, id=reply_id, user=request.user)
    
    if request.method == "POST":
        #question_id = reply.question.id  # Save the question ID before deleting
        reply_obj.delete()
        return redirect('question_detail',question_id = reply_obj.question.id)
    
    return redirect('question_detail', question_id=reply.question.id)

def search(request):
    query = request.GET.get('query')
    if query:
        results = questions.objects.filter(
            Q(question_text__icontains=query) |
            Q(user__username__icontains=query)
        ).order_by('-created_on')
    else:
        results = questions.objects.all().order_by('-created_on')

    return render(request, 'search.html', {'results': results, 'query': query})
