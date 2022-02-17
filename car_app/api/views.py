from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework import filters
from ..models import Car, CarRate
from .serializers import CarSerializer, CarRatingSerializer, CarPopularListSerializer



class CarViewset(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarPopularListViewset(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarPopularListSerializer    
              
class CarRate(viewsets.ModelViewSet):
    queryset = CarRate.objects.all()
    serializer_class = CarRatingSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rates_number']


