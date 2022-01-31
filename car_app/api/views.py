from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError
from ..models import Car
from .serializers import CarSerializer, CarRatingSerializer, CarPopularListSerializer


class CarViewset(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarPopularListViewset(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by("-rates_number")  
    serializer_class = CarPopularListSerializer
              
class CarRate(generics.CreateAPIView):
    serializer_class = CarRatingSerializer
    queryset = Car.objects.all()
 
    def perform_create(self, serializer):
        pk = serializer.validated_data['car_id']
        rating = serializer.validated_data['rating']
        queryset = Car.objects.all()
        car_queryset = get_object_or_404(queryset, pk=pk)
  
        if car_queryset.rates_number == 0:
            car_queryset.avg_rating = serializer.validated_data['rating']
        else:
            car_queryset.avg_rating = (car_queryset.avg_rating + serializer.validated_data['rating'])/2
            car_queryset.avg_rating = round(car_queryset.avg_rating, 1)

        car_queryset.rates_number = car_queryset.rates_number + 1
        car_queryset.save()
