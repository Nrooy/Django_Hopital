from rest_framework import serializers
from .models import Pharmaceutical, MedicalSupply

class PharmaceuticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmaceutical
        fields = '__all__'

class MedicalSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalSupply
        fields = '__all__'