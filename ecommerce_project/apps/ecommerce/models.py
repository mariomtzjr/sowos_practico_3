import uuid

from django.db import models
from django.contrib.auth.models import User as Usr

from apps.users.models import User


# Create your models here.
class Person(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)

    def save(self, *args, **kwargs):
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

        super().save(*args, **kwargs)


class Customer(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Purchase(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    iva = models.DecimalField(max_digits=5, decimal_places=2)
    subtotal = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PurchaseProducts(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    purchase_id = models.ForeignKey(Purchase, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
