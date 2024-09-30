from django.contrib import admin
from .models import ContactUs
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ContactUs)
class ContactUsAdmin(SummernoteModelAdmin):

    model = ContactUs
    list_display = (
         'contact_reason', 'email', 'phone_number', 'created_on',
        )

    summernote_fields = {'message'}

    ordering = ('created_on',)
