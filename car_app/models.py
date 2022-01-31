from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg, Sum

class Car(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0, blank=True)
    avg_rating = models.FloatField(default=0, blank=True)
    rates_number = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.make + ' ' + self.model

    