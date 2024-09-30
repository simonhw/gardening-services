from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import CONTACT_REASONS

from .forms import ContactUsForm
from accounts.models import UserAccount


def contact_us(request):
    """ View for the contact us page and form """

    if request.method == 'POST':
        contact_us_form = ContactUsForm(data=request.POST)
        if contact_us_form.is_valid():
            contact_us = contact_us_form.save(commit=False)
            contact_us.save()
            messages.success(
                request, 'Message successfully sent.'
            )
            _send_contact_email(contact_us_form)
            return redirect('home')
        else:
            contact_us_form = ContactUsForm(data=request.POST)
            return render(
                request, 'contact/contact_us.html',
                {
                    'contact_us_form': contact_us_form,
                }
            )

    if request.user.is_authenticated:
        try:
            account = UserAccount.objects.get(user=request.user)
            contact_us_form = ContactUsForm(initial={
                'full_name': account.user.get_full_name(),
                'email': account.user.email,
                'phone_number': account.default_phone_number,
            })
        except UserAccount.DoesNotExist:
            contact_us_form = ContactUsForm()
    else:
        contact_us_form = ContactUsForm()

    return render(
                request, 'contact/contact_us.html',
                {
                    'contact_us_form': contact_us_form,
                }
            )


def _send_contact_email(contact_us_form):
    """ Send the user a confirmation email. """

    full_name = contact_us_form.cleaned_data['full_name']
    cust_email = contact_us_form.cleaned_data['email']
    phone_number = contact_us_form.cleaned_data['phone_number']
    message = contact_us_form.cleaned_data['message']

    for key, label in CONTACT_REASONS:
        if key == contact_us_form.cleaned_data['contact_reason']:
            contact_reason = label

    subject = render_to_string(
        'contact/contact_emails/contact_email_subject.txt',
        {
            'contact_reason': contact_reason
        }
    )
    body = render_to_string(
        'contact/contact_emails/contact_email_body.txt',
        {
            'full_name': full_name,
            'email': cust_email,
            'phone_number': phone_number,
            'contact_reason': contact_reason,
            'message': message,
            'contact_email': settings.DEFAULT_FROM_EMAIL
        }
    )
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )


def subscribe_page(request):
    """
    View that renders the newsletter signup page.
    """

    return render(
        request,
        "contact/subscribe.html"
    )
