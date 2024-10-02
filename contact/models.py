from django.db import models
from accounts.models import UserAccount


class ContactUs(models.Model):
    """
    A custom model for the Contact Us form

    Fields:
        account (ForeignKey) - A foreign key to link the user's message
                               to their UserAccount if authenticated.
        full_name (CharField) - The user's full name
        email (EmailField) - The user's contact email
        phone_number (CharField) - The user's contact number
        contact_reason (CharField) - A specific reason for sending a
                                     message. Can only be selected from
                                     a dropdown list
        message (CharField) - The user's message content
        created_on - The date that the message was submitted
    """

    account = models.ForeignKey(
        UserAccount,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='contacts'
        )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    contact_reason = models.CharField(
        'Reason for Contacting Us', null=False, blank=False
        )
    message = models.CharField(max_length=500, blank=False)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.contact_reason
