import uuid

from django.db import models

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    provider_url = models.URLField()
    image = models.ImageField()
    date = models.DateTimeField()
    category = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)