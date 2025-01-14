from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from accounts.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model for the application, extending AbstractBaseUser and PermissionsMixin.

    This model includes a mobile number as the unique identifier for authentication
    and other basic user attributes. The model also supports permissions and is linked
    with the custom user manager.

    Attributes:
        mobile_number (CharField): The user's mobile number, used as the unique identifier.
        username (CharField): The user's username.
        first_name (CharField): The user's first name.
        last_name (CharField): The user's last name.
        date_joined (DateTimeField): The date and time when the user was created.
        is_active (BooleanField): Indicates whether the user is active.
        is_staff (BooleanField): Indicates whether the user has admin permissions.
    """

    mobile_number = models.CharField(
        max_length=31, unique=True,
        help_text="The user's mobile number, used as the unique identifier for authentication."
    )
    username = models.CharField(
        max_length=127, unique=True,
        help_text="The user's username, which must be unique across the system."
    )
    first_name = models.CharField(
        max_length=63,
        help_text="The user's first name."
    )
    last_name = models.CharField(
        max_length=63,
        help_text="The user's last name."
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
        help_text="The date and time when the user was created."
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Indicates whether the user is currently active."
    )
    is_staff = models.BooleanField(
        default=False,
        help_text="Indicates whether the user has staff (admin) permissions."
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'mobile_number'  # Set mobile_number as the unique identifier
    REQUIRED_FIELDS = ['username']  # Include other fields required during superuser creation

    def __str__(self):
        return self.mobile_number
