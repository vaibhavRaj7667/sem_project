from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class questions(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question_text = models.TextField(max_length=240)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question_text
    
class reply(models.Model):
    question = models.ForeignKey(questions, on_delete= models.CASCADE,related_name='replies')
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    reply_text = models.TextField(max_length=240)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reply_text
    
class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    


class QuestionReport(models.Model):
    reported_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_questions')
    reporting_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Report by {self.reporting_user.username} on {self.reported_user.username}'
