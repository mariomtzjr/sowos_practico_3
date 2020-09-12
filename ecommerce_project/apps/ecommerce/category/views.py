
from django.shortcuts import get_object_or_404, redirect

from rest_framework import generics
from rest_framework.response import Response

from apps.ecommerce.category.models import Category
from apps.ecommerce.api.serializers import CategorySerializer

# Create your views here.
class CategoryCreate(generics.CreateAPIView):
    serializer_class = CategorySerializer


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response({'categories': serializer.data})


class CategoryUpdate(generics.UpdateAPIView):
    serializer_class = CategorySerializer

    def put(self, request, pk):
        category = Category.objects.get(pk=pk)

        serializer = CategorySerializer(instance=category, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'category': category})
        serializer.save()
        return redirect('category_list')

class CategoryDelete(generics.DestroyAPIView):
    serializer_class = CategorySerializer

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return redirect('category_list')
