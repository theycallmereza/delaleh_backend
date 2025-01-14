from django.db import models

from authentication.utils import generate_api_key
from core.models import BaseModel


class Consumer(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    api_key = models.CharField(max_length=255, unique=True, default=generate_api_key)

    def __str__(self):
        return self.name
