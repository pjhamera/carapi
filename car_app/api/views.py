from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError
from ..models import Car, CarRate
from .serializers import CarSerializer, CarRatingSerializer, CarPopularListSerializer
from django.db.models import Count, F
from django.db.models.expressions import Window
from django.db.models.functions import Rank


class CarViewset(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarPopularListViewset(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarPopularListSerializer 
    
    def get_queryset(self, *args, **kwargs):
          rates_number = self.request.query_params.get('rates_number')
          cars = super().get_queryset()
          return cars.annotate(rates_number=Count('rates')).order_by('-rates_number')
              
class CarRate(viewsets.ModelViewSet):
    queryset = CarRate.objects.all()
    serializer_class = CarRatingSerializer
    


