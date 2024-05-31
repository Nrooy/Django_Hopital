from rest_framework import viewsets
from .models import Pharmaceutical, MedicalSupply
from .serializers import PharmaceuticalSerializer, MedicalSupplySerializer

class PharmaceuticalViewSet(viewsets.ModelViewSet):
    queryset = Pharmaceutical.objects.all()
    serializer_class = PharmaceuticalSerializer

class MedicalSupplyViewSet(viewsets.ModelViewSet):
    queryset = MedicalSupply.objects.all()
    serializer_class = MedicalSupplySerializer
