from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor, Position, Specialization, Schedule, Review
from .serializers import DoctorSerializer, PositionSerializer, SpecializationSerializer, ScheduleSerializer, ReviewSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned schedules to a given doctor,
        by filtering against a `doctor` query parameter in the URL.
        """
        queryset = Schedule.objects.all()
        doctor_id = self.request.query_params.get('doctor_id', None)
        if doctor_id is not None:
            queryset = queryset.filter(doctor_id=doctor_id)
        return queryset


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned reviews to a given doctor,
        by filtering against a `doctor` query parameter in the URL.
        """
        queryset = Review.objects.all()
        doctor_id = self.request.query_params.get('doctor_id', None)
        if doctor_id is not None:
            queryset = queryset.filter(doctor_id=doctor_id)
        return queryset


