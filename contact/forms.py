from .models import ContactUs
from django import forms
from django_recaptcha.fields import ReCaptchaField
from django.core.exceptions import ValidationError


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


    def clean(self):
        """
        Validation of form data on the back end.

        The method ensures that input fields cannot be blank.

        If the data validates, the method returns the cleaned data.
        If invalid, it raises a validation error to inform the user.
        """

        cleaned_data = super().clean()
        full_name = cleaned_data.get('full_name')
        email = cleaned_data.get('email')
        phone_number = cleaned_data.get('phone_number')
        contact_reason = cleaned_data.get('contact_reason')
        message = cleaned_data.get('message')
        captcha = cleaned_data.get('captcha')


        if not full_name:
            raise ValidationError('You must provide your full name.')

        if not email:
            raise ValidationError('You must provide a valid email.')

        if not phone_number:
            raise ValidationError('You must provide a phone number.')

        if not contact_reason:
            raise ValidationError('You must select a reason.')

        if not message:
            raise ValidationError('You must write a message.')

        if not captcha:
            raise ValidationError('You must complete the reCAPTCHA.')

        return cleaned_data
