from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.validators import validate_email


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            """captcha"""
            # recaptcha_response = request.POST.get('g-recaptcha-response')
            # url = 'https://www.google.com/recaptcha/api/siteverify'
            # payload = {
            #     'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            #     'response': recaptcha_response
            # }

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            inquiry = form.cleaned_data['inquiry']

            html = render_to_string('contact/emails/contactform.html',
                                    {'name': name,
                                     'email': email,
                                     'content': inquiry,
                                     })

            send_mail('Zapytanie dotyczące ... nr ...',
                      'Oto wiadomość',
                      f'',
                      ['robert.patryk.grzelak@gmail.com'],
                      html_message=html)

            messages.success(request, f'{name + "!" if name else ""} '
                                      f'Thank you for submitting an inquiry. We will get back to you ASAP.')
            return redirect('index')

        elif err := form.errors['email']:
            messages.error(request, err, 'danger')

        elif err := form.errors['inquiry']:
            messages.error(request, err, 'danger')

    else:
        form = ContactForm()

    return render(request, 'contact/index.html', {'form': form})
