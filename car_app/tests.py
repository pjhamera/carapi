from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Car

class CarAddListTest(APITestCase):

    def test_cars_list(self):
        response = self.client.get(reverse('cars-add-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_car_add(self):
        data = {
            "make": "Volvo",
            "model": "740 Series"
        }        
        response = self.client.post(reverse('cars-add-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
 
class CarDeleteTest(APITestCase): 

    def test_car_delete(self):
        self.car = Car.objects.create(
            make = "Volvo",
            model = "740 Series",
            rating = 5
        )
        response = self.client.delete(reverse('car-delete', args=(self.car.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CarRateTest(APITestCase):
        
    def test_rate_car(self):
        self.car = Car.objects.create(make = "Volvo", model = "780 Series")  
        data = {
            "car_id": self.car.id,
            "rating": 5
        }
        response = self.client.post(reverse('car-rate'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CarPopularListTest(APITestCase):

    def test_popular_list(self):
        response = self.client.get(reverse('cars-most-popular-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)