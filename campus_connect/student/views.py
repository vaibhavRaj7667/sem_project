from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login_page.html')

def register(request):
    return render(request,'register_user.html')