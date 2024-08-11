from django import forms 
#changes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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