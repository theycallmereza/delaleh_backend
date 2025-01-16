from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel

User = get_user_model()


# Create your models here.
class TelegramProfile(BaseModel):
    """
    Model to store the Telegram profile associated with a user.

    This model is linked to the custom user model via a one-to-one relationship,
    where each user can have one corresponding Telegram profile. It stores the
    unique Telegram ID of the user, which can be used for authentication or
    communication with the Telegram bot.

    Attributes:
        user (OneToOneField): The user to whom the Telegram profile belongs.
        telegram_id (CharField): The unique Telegram ID of the user.
        first_name (CharField): The first name of the Telegram user, used for personalization.
        last_name (CharField): The last name of the Telegram user, used for personalization (optional).
        username (CharField): The Telegram username, which can be used for non-ID-based identification (optional).
        language_code (CharField): The preferred language of the user, useful for adapting bot responses.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        help_text="The user associated with this Telegram profile, linking the Telegram account to the system's user.",
    )
    telegram_id = models.CharField(
        unique=True,
        max_length=127,
        help_text="The unique Telegram ID of the user, used for identifying and interacting with them via the bot.",
    )
    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=127,
        help_text="The first name of the Telegram user, stored for personalization purposes.",
    )
    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=127,
        help_text="The last name of the Telegram user, stored for personalization purposes (optional).",
    )
    username = models.CharField(
        null=True,
        blank=True,
        max_length=127,
        help_text="The Telegram username of the user, used for easier reference (optional).",
    )
    language_code = models.CharField(
        null=True,
        blank=True,
        max_length=127,
        help_text="The preferred language code of the user (e.g., 'en', 'fa'), used to adapt bot responses.",
    )


class UserProfile(BaseModel):
    """
    Model to store additional profile information for a user.

    This model extends the base user model by adding optional fields
    to store detailed profile information such as name, birth date,
    bio, height, profile image, and location coordinates.

    Attributes:
        user (OneToOneField): A one-to-one relationship linking this profile to a specific user.
        name (CharField): The full name of the user (optional).
        birth_date (DateField): The user's date of birth (optional).
        bio (TextField): A brief biography or description of the user (optional).
        height (IntegerField): The user's height in centimeters (optional).
        image (ImageField): A profile image for the user, stored in the "profile_images" directory (optional).
        latitude (FloatField): The latitude coordinate of the user's location (optional).
        longitude (FloatField): The longitude coordinate of the user's location (optional).
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        help_text="The user associated with this profile, linking additional details to a specific user.",
    )
    name = models.CharField(null=True, blank=True, max_length=127, help_text="The full name of the user (optional).")
    birth_date = models.DateField(
        null=True,
        blank=True,
        help_text="The user's date of birth, useful for personalization or age-based features (optional).",
    )
    bio = models.TextField(null=True, blank=True, help_text="A brief biography or description of the user (optional).")
    height = models.IntegerField(null=True, blank=True, help_text="The user's height in centimeters (optional).")
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="profile_images",
        help_text="A profile image for the user, stored in the 'profile_images' directory (optional).",
    )
    latitude = models.FloatField(
        null=True,
        blank=True,
        help_text="The latitude coordinate of the user's location, used for geolocation features (optional).",
    )
    longitude = models.FloatField(
        null=True,
        blank=True,
        help_text="The longitude coordinate of the user's location, used for geolocation features (optional).",
    )
