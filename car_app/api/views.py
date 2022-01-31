import sys
import urllib.request
import json
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
          
      
# class CarAddList(generics.ListCreateAPIView):
#     serializer_class = CarSerializer
#     queryset = Car.objects.all()

#     def perform_create(self, serializer):
#         make = serializer.validated_data['make']
#         model = serializer.validated_data['model']
#         car_queryset = Car.objects.filter(make=make, model=model)
#         car_database = check_car_in_database(make)
#         car_models = car_database['Results']
#         models = []
#         for car_model in car_models:
#             models.append(car_model['Model_Name'])
#         if model not in models:
#             raise ValidationError("This car does not exist")    
#         if car_queryset.exists():
#             raise ValidationError("You have already added this car!")
#         else:
#            serializer.save()     

# class CarDelete(generics.DestroyAPIView):
#     serializer_class = CarSerializer

#     def get_queryset(self):
#         queryset = Car.objects.filter(id=self.kwargs['pk'])
#         return queryset
    
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

# class CarPopularList(generics.ListAPIView):
#     serializer_class = CarPopularListSerializer
#     queryset = Car.objects.all().order_by("-rates_number")
