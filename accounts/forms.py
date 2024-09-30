from django.contrib.auth.forms import UserChangeForm
from allauth.account.forms import SignupForm, LoginForm, ResetPasswordForm
from .models import CustomUser
from django import forms
from .models import UserAccount


class CustomUserCreationForm(SignupForm):
    """ Specify the model used for creating a user """

    first_name = forms.CharField(
        max_length=35,
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name *'
            }
        )
        )

    last_name = forms.CharField(
        max_length=35,
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name *'
            }
        )
        )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name *'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name *'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email Address *'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'username' in self.fields:
            del self.fields['username']
        self.fields['email'].label = ''
        self.fields['email'].widget = forms.EmailInput(
            attrs={
                'placeholder': 'Email Address *'
                }
            )
        self.fields['email2'].label = ''
        self.fields['email2'].widget = forms.EmailInput(
            attrs={
                'placeholder': 'Confirm Email Address *'
                }
            )
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Password *'
                }
            )
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm Password *'
                }
            )

    field_order = [
        'first_name',
        'last_name',
        'email',
        'email2',
        'password1',
        'password2',
    ]

    def try_save(self, request):
        """
        This method is added because allauth expects it when handling
        the saving process
        """
        user = self.save(request)
        return user, None


class CustomLoginForm(LoginForm):
    """ A custom login form to allow for customisation """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['login'].label = ''
        self.fields['password'].label = ''


class CustomResetPasswordForm(ResetPasswordForm):
    """ A custom login form to allow for cusomisation """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].label = ''


class CustomUserChangeForm(UserChangeForm):
    """ Specify the model used for editing a user """

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')


class UserAccountForm(forms.ModelForm):
    """
    Form to handle updating user details.
    """

    class Meta:
        model = UserAccount
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County',
            'default_eircode': 'Eircode',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
