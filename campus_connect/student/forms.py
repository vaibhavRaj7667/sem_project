from django import forms 
#changes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import questions
from .models import reply


class Student_user_creation_form(UserCreationForm): # need to import in views
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields =('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class QuestionForm(forms.ModelForm):
    class Meta:
        model = questions
        fields =['question_text']
        widgets = {
            'question_text': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

# class replyfrom(forms.ModelForm):
#     class Meta:
#         model = reply
#         fields = ['reply_text']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = reply
        fields = ['reply_text']  # Only include the text field in the form
        widgets = {
            'reply_text': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }