from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'cars', views.CarViewset)
router.register(r'rate', views.CarRate)
router.register(r'popular', views.CarPopularListViewset)



