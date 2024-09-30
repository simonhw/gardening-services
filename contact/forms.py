from .models import ContactUs
from django import forms
from django_recaptcha.fields import ReCaptchaField


CONTACT_REASONS = (
    ('', 'Reason for Contacting Us *'),
    ('service_inquiry', 'Service Inquiry'),
    ('quote_request', 'Request a Quote'),
    ('cancel_reschedule', 'Cancellation or Rescheduling'),
    ('general_inquiry', 'General Inquiries'),
    ('other', 'Other'),
)


class ContactUsForm(forms.ModelForm):
    """
    A form for sending a message to the business owners
    """

    captcha = ReCaptchaField(required=True)

    class Meta:
        """
        Meta class for the form's metadata. Specifies the model to use
        and which fields to display to the user.
        """

        model = ContactUs
        fields = {
            'full_name',
            'email',
            'phone_number',
            'contact_reason',
            'message',
        }
        widgets = {
            'contact_reason': forms.Select(
                choices=CONTACT_REASONS,
                attrs={
                    'class': 'select-placeholder'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'style': 'height: 200px;'
                }
            )
        }

    field_order = [
        'full_name',
        'email',
        'phone_number',
        'contact_reason',
        'message',
    ]

    def __init__(self, *args, **kwargs):
        """ Add placeholders and remove labels """

        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'contact_reason': 'Reason for Contacting Us',
            'message': 'Message',
        }

        for field in self.fields:
            if field == 'captcha':
                self.fields[field].label = ''
                continue
            elif field == 'contact_reason':
                self.fields[field].label = False
                continue
            elif self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
