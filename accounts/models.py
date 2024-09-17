from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUserManager(BaseUserManager):
    """ Model for creating user accounts """

    def create_user(
        self, email, password, first_name, last_name, **extra_fields
        ):
        """
        Create a user with a supplied email, password, and first and
        last name
        """

        if not email:
            raise ValueError(_('You must set an email!'))
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(
        self, email, password, first_name, last_name, **extra_fields
        ):
        """
        Create a superuser with a supplied email, password and first
        and last name. Add the additional fields of is_staff,
        is_active, and is_superuser.
        """

        super = self.create_user(
            email, password, first_name, last_name, **extra_fields
            )

        super.is_staff = True
        print('super.is_staff =', super.is_staff)
        super.is_active = True
        print('super.is_active =', super.is_active)
        super.is_superuser = True
        print('super.is_superuser =', super.is_superuser)

        if super.is_staff is not True:
            raise ValueError(
                _('Superuser must have is_staff=True')
            )
        if super.is_superuser is not True:
            raise ValueError(
                _('Superuser must have is_superuser=True')
            )
        super.save()
        return super


class CustomUser(AbstractUser, PermissionsMixin):
    """
    Custom User model which takes the user's email as their username
    """

    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=35, blank=True)
    last_name = models.CharField(_('last name'), max_length=35, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    objects = CustomUserManager()
    def __str__(self):
        return self.email