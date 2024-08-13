from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('delete/<int:question_id>/', views.delete_question, name='delete_question'),
    path('logout/', views.logout_view, name='logout'),

]