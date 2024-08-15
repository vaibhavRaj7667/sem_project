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