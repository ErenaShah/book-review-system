from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Comment
from django import forms
from django.forms.widgets import PasswordInput, TextInput


class CreateUserForm(UserCreationForm):

    class Meta:

        model=User
        fields=['username','email','password1','password2']


class LoginForm(AuthenticationForm):

    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())


class FeedbackForm(forms.ModelForm):
    class Meta:
        model= Comment 
        fields="__all__"
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('name', 'email', 'body')