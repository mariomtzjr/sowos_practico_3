from rest_framework import serializers

from apps.ecommerce.person.models import Person
from apps.ecommerce.customer.models import Customer
from apps.ecommerce.purchase.models import Purchase
from apps.ecommerce.purchaseproduct.models import PurchaseProducts
from apps.ecommerce.product.models import Product
from apps.ecommerce.category.models import Category


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'name',
            'last_name',
        )
        read_only_fields = ('id','created_at', 'updated_at',)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        return instance


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'id',
            'person_id',
            'is_active',
            'is_deleted',
        )
        read_only_fields = ('id', 'created_at', 'updated_at',)


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
