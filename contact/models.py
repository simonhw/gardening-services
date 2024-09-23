from django.db import models
from accounts.models import UserAccount


class ContactUs(models.Model):
    """ A model for the Contact Us form """

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

    class Meta:
        verbose_name_plural: 'Contact Us Messages'

    def __str__(self):
        return self.contact_reason