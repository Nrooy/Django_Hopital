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
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

# Ví dụ với Review


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


