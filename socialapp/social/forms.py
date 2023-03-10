from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
