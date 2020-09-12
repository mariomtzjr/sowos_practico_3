
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


class PurchaseUpdate(generics.UpdateAPIView):
    serializer_class = PurchaseSerializer

    def put(self, request, pk):
        purchase = Purchase.objects.get(pk=pk)

        serializer = PurchaseSerializer(instance=purchase, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'purchase': purchase})
        serializer.save()
        return redirect('purchase_list')

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
