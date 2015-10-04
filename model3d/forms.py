__author__ = 'fgautier'

from django import forms

class AddModelForm(forms.Form):
    title = forms.CharField(max_length=180)
    description = forms.CharField(widget=forms.Textarea, max_length=255)