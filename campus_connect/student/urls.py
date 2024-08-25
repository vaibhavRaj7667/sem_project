from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('delete/<int:question_id>/', views.delete_question, name='delete_question'),
    path('logout/', views.logout_view, name='logout'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    #path('reply/delete/<int:reply_id>/', views.delete_reply, name='delete_reply'),
    # path('question/<int:question_id>/',views.question_detail,name='question_detail'),
    path('reply/delete/<int:reply_id>/', views.delete_reply, name='delete_reply'),
    path('search/',views.search,name='seach'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    
]