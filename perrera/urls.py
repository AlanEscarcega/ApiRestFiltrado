from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PerroViewSet

router = DefaultRouter()
router.register(r"perros", PerroViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
