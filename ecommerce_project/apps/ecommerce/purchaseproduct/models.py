from django.db import models

from apps.ecommerce.product.models import Product
from apps.ecommerce.purchase.models import Purchase

# Create your models here.
class PurchaseProducts(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    purchase_id = models.ForeignKey(Purchase, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "purchaseproduct"
        verbose_name_plural = "purchaseproducts"
