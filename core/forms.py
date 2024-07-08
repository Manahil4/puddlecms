from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from core.models import CustomUser  # Update this import to your custom user model

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Username',
        'class':'w-full py-4 px-6 rounded-xl'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
        'class':'w-full py-4 px-6 rounded-xl'}))
    
    

class SignupForm(UserCreationForm):
    class Meta:
        model= CustomUser
        fields = ('username','email','password1','password2', 'is_designer')

    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Username',
        'class':'w-full py-4 px-6 rounded-xl'}))
    
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Email',
        'class':'w-full py-4 px-6 rounded-xl'}))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
        'class':'w-full py-4 px-6 rounded-xl'}))
    
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repeat Password',
        'class':'w-full py-4 px-6 rounded-xl'}))
    
    is_designer = forms.BooleanField(required=False, label="Are you a designer?")
    
