from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from Admin.models import User
from Bet.models import *

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Enter Your Email'
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Enter Your Password'
    }))

    class Meta:
        model = CustomUser
        fields = ('email','password1')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'First Name'
    }))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Last Name'
    }))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Username',
        'autocomplete': 'off' 
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Email',
        'autocomplete': 'off'
    }))
    password1 = forms.CharField( max_length=20, label='Password' ,widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Password',
        'autocomplete': 'off'
    }))
    password2 = forms.CharField( max_length=20, label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Confirm Password',
        'autocomplete': 'off'
    }))

    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','username','email','password1','password2')



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ('email','password')


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser 
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['dob', 'phone_number', 'address_city']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'phone_number': forms.NumberInput(),
            'address_city': forms.TextInput(),
        }

