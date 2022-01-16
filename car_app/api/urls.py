from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.CarAddList.as_view(), name='cars-add-list'),
    path('cars/<int:pk>/', views.CarDelete.as_view(), name='car-delete'),
    path('rate/', views.CarRate.as_view(), name='car-rate'),
    path('popular/', views.CarPopularList.as_view(), name='cars-most-popular-list')
]
