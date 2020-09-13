
from django.shortcuts import get_object_or_404, redirect

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from apps.ecommerce.purchase.models import Purchase
from apps.ecommerce.purchaseproduct.models import PurchaseProducts
from apps.ecommerce.api.serializers import PurchaseProductsSerializer

# Create your views here.
class BaseView():
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class PurchaseProductsCreate(BaseView, generics.CreateAPIView):
    serializer_class = PurchaseProductsSerializer

    def post(self, request):
        serializer = PurchaseProductsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'purchase_product': purchase_product})
        serializer.save()
        Purchase.update_purchase_data()
        return redirect('purchaseproduct_list')



class PurchaseProductsList(BaseView, generics.ListAPIView):
    serializer_class = PurchaseProductsSerializer

    def get(self, request, *args, **kwargs):
        queryset = PurchaseProducts.objects.all()
        serializer = PurchaseProductsSerializer(queryset, many=True)
        return Response({'purchase-products': serializer.data})


class PurchaseProductsUpdate(BaseView, generics.UpdateAPIView):
    serializer_class = PurchaseProductsSerializer

    def put(self, request, pk):
        purchase_product = PurchaseProducts.objects.get(pk=pk)

        serializer = PurchaseProductsSerializer(instance=purchase_product, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'purchase_product': purchase_product})
        serializer.save()
        return redirect('pruchaseproduct_list')

class PurchaseProductsDelete(BaseView, generics.DestroyAPIView):
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
