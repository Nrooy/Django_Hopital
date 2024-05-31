from rest_framework import serializers
from .models import MedicalRecord, Prescription
from bson.objectid import ObjectId

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'
        extra_kwargs = {
            '_id': {'read_only': True}
        }

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'
        extra_kwargs = {
            '_id': {'read_only': True}
        }
        
    def create(self, validated_data):
        prescriptions_data = validated_data.pop('prescriptions')
        medical_record = MedicalRecord.objects.create(**validated_data)
        for prescription_data in prescriptions_data:
            Prescription.objects.create(medical_record=medical_record, **prescription_data)
        return medical_record
