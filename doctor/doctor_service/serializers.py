from rest_framework import serializers
from .models import Specialization, Position, Doctor, Schedule, Review
from django.core.validators import MinValueValidator, MaxValueValidator



class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    specialization = SpecializationSerializer(required=False)
    position = PositionSerializer(required=False)
    specialization_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Specialization.objects.all(), source='specialization')
    position_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Position.objects.all(), source='position')
    class Meta:
        model = Doctor
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(required=False)
    doctor_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Doctor.objects.all(), source='doctor')
    class Meta:
        model = Schedule
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(required=False)
    doctor_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Doctor.objects.all(), source='doctor')
    class Meta:
        model = Review
        fields = '__all__'
        extra_kwargs = {
            'rating': {
                'validators': [MinValueValidator(1), MaxValueValidator(5)],
            },
        }
