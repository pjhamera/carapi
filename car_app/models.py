from django.db import models
from django.db.models import Avg
from django.core.validators import MinValueValidator, MaxValueValidator


class Car(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)

    # @property
    # def rates_number(self):
    #     rates_number = self.rates.all().count()
    #     return rates_number

    @property
    def avg_rating(self):
        avg_rating = self.rates.all().aggregate(Avg('rating')).values()
        return avg_rating

    def __str__(self):
        return self.make + ' ' + self.model


class CarRate(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='rates')

