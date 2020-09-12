from rest_framework import serializers

from apps.ecommerce.models import (
    Person,
    Customer,
    Purchase,
    PurchaseProducts,
    Product,
    Category,
)


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'name',
            'last_name',
        )
        read_only_fields = ('created_at', 'updated_at',)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'id',
            'person_id',
            'is_active',
            'is_deleted',
        )
        read_only_fields = ('created_at', 'updated_at',)


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = (
            'id',
            'customer_id',
            'iva',
            'subtotal',
            'total'
        )
        read_only_fields = ('created_at', 'updated_at',)


class PurchaseProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseProducts
        fields = (
            'id',
            'product_id',
            'purchase_id',
            'quantity',
        )
        read_only_fields = ('created_at', 'updated_at',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'category_id',
            'name',
            'description',
            'quantity',
            'price'
        )
        read_only_fields = ('created_at', 'updated_at',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'description',
        )
        read_only_fields = ('created_at', 'updated_at',)
