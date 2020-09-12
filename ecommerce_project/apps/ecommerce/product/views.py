
from django.shortcuts import get_object_or_404, redirect

from rest_framework import generics
from rest_framework.response import Response

from apps.ecommerce.product.models import Product
from apps.ecommerce.api.serializers import ProductSerializer

# Create your views here.
class ProductCreate(generics.CreateAPIView):
    serializer_class = ProductSerializer


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response({'products': serializer.data})


class ProductUpdate(generics.UpdateAPIView):
    serializer_class = ProductSerializer

    def put(self, request, pk):
        product = Product.objects.get(pk=pk)

        serializer = ProductSerializer(instance=product, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'product': product})
        serializer.save()
        return redirect('product_list')

class ProductDelete(generics.DestroyAPIView):
    serializer_class = ProductSerializer

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return redirect('product_list')