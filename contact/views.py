from django.shortcuts import render
from .models import ContactUs
from .forms import ContactUsForm
from accounts.models import UserAccount


def contact_us(request):
    """ View for the contact us page and form """

    if request.method == 'POST':
        contact_us_form = ContactUsForm(data=request.POST)
        if contact_us_form.is_valid:
            contact_us = contact_us_form.save(commit=False)
            if request.user.is_authenticated:
                contact_us.account = request.user
            contact_us.save()
            return redirect('home')
            messagess.success(
                request, 'Message successfully sent.'
            )
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
