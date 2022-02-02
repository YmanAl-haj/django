from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, ModelForm, ChoiceField

from . import models
from .models import Customer

class UserInfoForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']
        widgets = {
            'name': TextInput(attrs={
                'class': "w3-input w3-border w3-margin-bottom",
                'placeholder': 'Enter Username'
                }),
            'email': EmailInput(attrs={
                'class': "w3-input w3-border w3-margin-bottom",
                'placeholder': 'Enter Email'
                }),
        }