from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils import timezone

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    Define how user instances are displayed on the Django admin site.
    """

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = CustomUser
    list_display = (
        'email', 'first_name', 'last_name',
        'is_staff', 'is_superuser', 'is_active',
        )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_staff','is_superuser',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)