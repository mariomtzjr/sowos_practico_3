from django.db import models
from apps.users.models import User


# Create your models here.
class Person(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class Customer(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Purchase(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL)
    iva = models.DecimalField()
    subtotal = models.DecimalField()
    total = models.DecimalField()


class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField()


class PurchaseProducts(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL)
    purchase_id = models.ForeignKey(Purchase, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
