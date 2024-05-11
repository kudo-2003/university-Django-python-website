# library Django 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#form Sign Up []
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    address = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone_number', 'address', 'password1', 'password2',)
