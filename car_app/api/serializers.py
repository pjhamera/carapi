from rest_framework import serializers
from ..models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'avg_rating')
        read_only_fields = ('id', 'avg_rating')

class CarRatingSerializer(serializers.ModelSerializer):
    car_id = serializers.IntegerField()
    class Meta:
        model = Car
        fields = ('car_id', 'rating')           

class CarPopularListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'rates_number')    