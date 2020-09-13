import uuid

from django.db import models
from django.contrib.auth.models import User as Usr

from apps.users.models import User


class Person(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "person"
        verbose_name_plural = "persons"

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)

    def save(self, *args, **kwargs):
        if not self.pk:
            username = "{}{}-{}".format(
                self.name.lower(),
                self.last_name.lower(),
                str(uuid.uuid4())[:5]
            )
            user = Usr.objects.create(
                username=username,
                first_name=self.name,
                last_name=self.last_name
            )
            user.save()
            user_app = User.objects.create(
                user=user,
                uuid=str(uuid.uuid4())[:36]
            )
            user_app.save()

            self.user_id = user_app

        super(Person, self).save(*args, **kwargs)
