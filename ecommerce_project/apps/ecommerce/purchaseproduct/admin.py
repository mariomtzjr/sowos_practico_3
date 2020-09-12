from django.contrib import admin

from .models import PurchaseProducts

@admin.register(PurchaseProducts)
class PurchaseProductsAdmin(admin.ModelAdmin):
    pass
