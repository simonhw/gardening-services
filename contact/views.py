from django.shortcuts import render
from .models import ContactUs


def contact_us(request):
    """ View for the contact us page """

    return render(request, 'contact/contact_us.html')
