from django.db import models

from apps.ecommerce.customer.models import Customer


class Purchase(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    iva = models.DecimalField(max_digits=5, decimal_places=2)
    subtotal = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "purchase"
        verbose_name_plural = "purchases"

    def __str__(self):
        return "{}-{}".format(self.id, self.customer_id)
