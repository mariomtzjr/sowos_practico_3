from django.contrib import admin

from .models import Product

@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    pass
