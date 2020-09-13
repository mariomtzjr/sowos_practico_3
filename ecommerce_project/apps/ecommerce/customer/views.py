
from django.shortcuts import get_object_or_404, redirect

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from apps.ecommerce.customer.models import Customer
from apps.ecommerce.api.serializers import CustomerSerializer

# Create your views here.
class BaseView():
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

class CustomerCreate(BaseView, generics.CreateAPIView):
    serializer_class = CustomerSerializer


class CustomerList(BaseView, generics.ListAPIView):
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response({'customers': serializer.data})


class CustomerUpdate(BaseView, generics.UpdateAPIView):
    serializer_class = CustomerSerializer

    def put(self, request, pk):
        customer = Customer.objects.get(pk=pk)

        serializer = CustomerSerializer(instance=customer, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'customer': customer})
        serializer.save()
        return redirect('customer_list')

class CustomerDelete(BaseView, generics.DestroyAPIView):
    serializer_class = CustomerSerializer

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        customer = self.get_object(pk)
        customer.delete()
        return redirect('customer_list')
