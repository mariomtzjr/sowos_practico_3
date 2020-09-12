
from django.shortcuts import get_object_or_404, redirect

from rest_framework import generics
from rest_framework.response import Response

from apps.ecommerce.purchaseproduct.models import PurchaseProducts
from apps.ecommerce.api.serializers import PurchaseProductsSerializer

# Create your views here.
class PurchaseProductsCreate(generics.CreateAPIView):
    serializer_class = PurchaseProductsSerializer


class PurchaseProductsList(generics.ListAPIView):
    serializer_class = PurchaseProductsSerializer

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = PurchaseProductsSerializer(queryset, many=True)
        return Response({'purchase-products': serializer.data})


class PurchaseProductsUpdate(generics.UpdateAPIView):
    serializer_class = PurchaseProductsSerializer

    def put(self, request, pk):
        purchase_product = PurchaseProducts.objects.get(pk=pk)

        serializer = PurchaseProductsSerializer(instance=purchase_product, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'purchase_product': purchase_product})
        serializer.save()
        return redirect('pruchaseproduct_list')

class PurchaseProductsDelete(generics.DestroyAPIView):
    serializer_class = PurchaseProductsSerializer

    def get_object(self, pk):
        try:
            return PurchaseProducts.objects.get(pk=pk)
        except PurchaseProducts.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        pruchase_product = self.get_object(pk)
        purchase_product.delete()
        return redirect('purchaseproduct_list')
