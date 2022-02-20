from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from ..models import Car, CarRate
from ..models_in_database import models_from__database

class CarSerializer(serializers.ModelSerializer): 
    
    def validate(self, attrs):
        make = attrs['make']
        model = attrs['model']
        car_queryset = Car.objects.filter(make=make, model=model)
        car_models_in_database = models_from__database(make)
        
        if model not in car_models_in_database :
            raise ValidationError("This car does not exist")    
        if car_queryset.exists():
            raise ValidationError("You have already added this car!")
        return attrs 

    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'avg_rating')
        read_only_fields = ('id', 'avg_rating')

class CarRatingSerializer(serializers.ModelSerializer):
    car_id = serializers.IntegerField()
    
    class Meta:
        model = CarRate
        fields = ('car_id', 'rating')           

class CarPopularListSerializer(serializers.ModelSerializer):
    rates_number = serializers.IntegerField()

    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'rates_number')  
        
        

        




       