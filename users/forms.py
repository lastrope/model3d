__author__ = 'fgautier'

from django import forms
"""
LoginForm
Provide a login form for all existing user
"""
class LoginForm(forms.Form):
    login = forms.CharField(label='Login')
    password = forms.CharField(widget=forms.PasswordInput)
