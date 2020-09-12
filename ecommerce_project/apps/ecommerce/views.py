import uuid

from django.shortcuts import render
from django.contrib.auth.models import User as Usr

from rest_framework import status, generics
from rest_framework.response import Response

from apps.users.models import User
from apps.ecommerce.models import Person
from apps.ecommerce.api.serializers import PersonSerializer


# Create your views here.
class PersonCreate(generics.CreateAPIView):
    serializer_class = PersonSerializer
