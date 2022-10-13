from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    inquiry = forms.CharField(widget=forms.Textarea)
