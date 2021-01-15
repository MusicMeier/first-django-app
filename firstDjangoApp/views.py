from django.shortcuts import render
from .models import Dog
from .serializers import DogSerializer
from rest_framework import viewsets

class DogView(viewsets.ModelViewSet):
  queryset = Dog.objects.all()
  serializer_class = DogSerializer