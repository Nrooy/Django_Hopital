from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PharmaceuticalViewSet, MedicalSupplyViewSet

router = DefaultRouter()
router.register(r'pharmaceuticals', PharmaceuticalViewSet)
router.register(r'medical-supplies', MedicalSupplyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
