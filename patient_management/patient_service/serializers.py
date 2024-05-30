from rest_framework import serializers
from .models import Patient, MedicalHistory


class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    medical_history = MedicalHistorySerializer(many=True)

    class Meta:
        model = Patient
        fields = "__all__"
