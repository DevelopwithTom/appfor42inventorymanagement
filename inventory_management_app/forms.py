from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Email'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))


    # def __init__(self, *args, **kwargs):
    #     self.error_messages['invalid_login'] = 'Custom error'
    #     super().__init__(*args, **kwargs)
