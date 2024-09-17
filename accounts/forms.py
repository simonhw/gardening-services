from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """ Specify the model used for creating a user """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')


class CustomUserChangeForm(UserChangeForm):
    """ Specify the model used for editing a user """

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')