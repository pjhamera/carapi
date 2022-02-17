from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.CarViewset.as_view({'get': 'list', 'post': 'create'}), name='cars-add-list'),
    path('cars/<int:pk>/', views.CarViewset.as_view({'delete': 'destroy'}), name='car-delete'),
    path('rate/', views.CarRate.as_view({'post': 'create'}), name='car-rate'),
    path('popular/', views.CarPopularListViewset.as_view({'get': 'list'}), name='cars-most-popular-list')
]

