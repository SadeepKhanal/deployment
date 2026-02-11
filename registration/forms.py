from django import forms
from .models import Registration
import re
class RegistrationForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        # error_messages={'required': 'Name is required'}
    )
    email = forms.EmailField(
        error_messages={
            'required': 'Email is required',
            'invalid': 'Please enter a valid email'
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={'required': 'Password is required'}
    )
    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z\d\s]).{8,}$'
        if not len(password)>=8:
            raise forms.ValidationError(
                "password must be 8 character "
            )
            
        return password