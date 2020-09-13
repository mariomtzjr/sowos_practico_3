
from django.shortcuts import get_object_or_404, redirect

from rest_framework import generics
from rest_framework.response import Response

from apps.ecommerce.purchase.models import Purchase
from apps.ecommerce.api.serializers import PurchaseSerializer

# Create your views here.
class PurchaseCreate(generics.CreateAPIView):
    serializer_class = PurchaseSerializer


class PurchaseList(generics.ListAPIView):
    serializer_class = PurchaseSerializer

    def get(self, request, *args, **kwargs):
        queryset = Purchase.objects.all()
        serializer = PurchaseSerializer(queryset, many=True)
        return Response({'purchases': serializer.data})


class PurchaseDelete(generics.DestroyAPIView):
    serializer_class = PurchaseSerializer

    def get_object(self, pk):
        try:
            return Purchase.objects.get(pk=pk)
        except Purchase.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        purchase = self.get_object(pk)
        purchase.delete()
        return redirect('purchase_list')
