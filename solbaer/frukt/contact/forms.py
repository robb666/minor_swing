from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=31,  # label='Name', .label_tag error_messages={'invalid': 'Message is too short'}
                           widget=forms.TextInput(attrs={'class': "form-control",
                                                         'id': 'firstname',
                                                         'placeholder': 'Your name'}), required=False)

    email = forms.EmailField(error_messages={'invalid': 'Please check your email.'},
                             widget=forms.TextInput(attrs={'class': "form-control",
                                                           'id': 'email',
                                                           'placeholder': 'Enter email'}), required=True)

    inquiry = forms.CharField(error_messages={'invalid': 'Message is too short'}, min_length=5,
                              widget=forms.Textarea(attrs={'class': "form-control",
                                                           'id': 'inquiry',
                                                           'placeholder': 'Content...',
                                                           'rows': 5}), required=True)
