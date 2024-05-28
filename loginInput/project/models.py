from django.db import models

from django import forms

class AddPostForm(forms.Form):
    summary = forms.Textarea()
    password = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    remember_me = forms.BooleanField()