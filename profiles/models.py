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
            telegram_id (CharField): The unique Telegram ID of the user, used for bot interactions.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                help_text="The user associated with this Telegram profile."
                                )
    telegram_id = models.CharField(unique=True,
                                   max_length=127,
                                   help_text="The unique Telegram ID of the user, used for interacting with the bot."
                                   )
