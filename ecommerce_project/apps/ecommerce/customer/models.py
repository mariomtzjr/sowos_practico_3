from django.db import models

from apps.ecommerce.person.models import Person

class Customer(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        full_name = "{} {}".format(
            self.person_id.name,
            self.person_id.last_name
        )
        return full_name
