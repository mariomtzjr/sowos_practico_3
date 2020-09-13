from collections import Counter
from decimal import Decimal

from django.db import models

from apps.ecommerce.customer.models import Customer
from apps.ecommerce.product.models import Product


class Purchase(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    iva = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    subtotal = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "purchase"
        verbose_name_plural = "purchases"

    def __str__(self):
        return "{}-{}".format(self.id, self.customer_id)

    def get_products_from_purchaseproducts(self):
        purchases = PurchaseProducts.objects.filter(purchase_id__id=self.id)
        products = dict(Counter([Product.objects.get(id=product.product_id.id) for product in purchases]))

        return products
        
    @property
    def update_purchase_data(self):
        self.subtotal = 0
        self.iva = 0.15
        for p, q in self.get_products_from_purchaseproducts():
            product = Product.objects.get(id=p.id)
            if product.quantity > 0:
                product.quantity -= q
                self.subtotal += product.price * q
        self.total = self.subtotal + (self.subtotal * Decimal(self.iva))
