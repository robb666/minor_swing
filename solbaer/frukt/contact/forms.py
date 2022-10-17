from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"id": "email", "onkeyup": "validateEmail()"}),
    )

    inquiry = forms.CharField(widget=forms.Textarea(attrs={'rows': 10}))





