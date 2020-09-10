import uuid

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=36)

    def save(self, *args, **kwargs):
        self.uuid = str(uuid.uuid4())[:36]

        super().save(*args, **kwargs)
