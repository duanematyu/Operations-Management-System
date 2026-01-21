from .models import AbstractUser
from django import forms
class UserForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField()
    class Meta:
        model = AbstractUser
        fields = ['username', 'password']