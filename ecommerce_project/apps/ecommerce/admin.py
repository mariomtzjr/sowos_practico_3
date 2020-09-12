from django.contrib import admin

from apps.ecommerce.person.models import Person
from apps.ecommerce.category.models import Category
from apps.ecommerce.customer.models import Customer
from apps.ecommerce.purchase.models import Purchase
from apps.ecommerce.purchaseproduct.models import PurchaseProducts

from apps.users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(PurchaseProducts)
class PurchaseProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    pass
