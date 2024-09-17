from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """
    Specify the model used for creating a user via the Django admin
    page.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'email', 'password',
            'is_staff', 'is_active', 'is_superuser'
            )


class CustomUserChangeForm(UserChangeForm):
    """
    Specify the model used for editing a user via the Django admin
    page.
    """

    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'email', 'password',
            'is_staff', 'is_active', 'is_superuser'
            )