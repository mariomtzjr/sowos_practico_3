from django.shortcuts import get_object_or_404, redirect

from rest_framework import generics
from rest_framework.response import Response

from apps.ecommerce.person.models import Person
from apps.ecommerce.api.serializers import PersonSerializer

# Create your views here.
class PersonCreate(generics.CreateAPIView):
    serializer_class = PersonSerializer


class PersonList(generics.ListAPIView):
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        queryset = Person.objects.all()
        serializer = PersonSerializer(queryset, many=True)
        return Response({'persons': serializer.data})


class PersonUpdate(generics.UpdateAPIView):
    serializer_class = PersonSerializer

    def put(self, request, pk):
        person = Person.objects.get(pk=pk)

        serializer = PersonSerializer(instance=person, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'person': person})
        serializer.save()
        return redirect('person_list')

class PersonDelete(generics.DestroyAPIView):
    serializer_class = PersonSerializer

    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        person = self.get_object(pk)
        person.delete()
        return redirect('person_list')
