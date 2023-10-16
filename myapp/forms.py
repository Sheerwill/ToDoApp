from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import ToDoModel
from django.contrib.auth.models import User

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoModel
        fields = ["entry"]   

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']