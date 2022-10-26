from django import forms
from django.db import models

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.Textarea, required=False)
    # email = forms.EmailField(),

    email = forms.EmailField(
        widget=forms.TextInput(attrs={"id": "email"}),
    )
    # record = forms.BooleanField()
    inquiry = forms.CharField(widget=forms.Textarea(attrs={'rows': 10}))





