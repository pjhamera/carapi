from django.contrib import admin
from django.urls import path, include
from car_app.api.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
