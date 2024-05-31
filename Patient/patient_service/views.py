from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import HealthInsurance ,Patient
from .serializers import HealthInsuranceSerializer ,PatientSerializer

class HealthInsuranceCreateView(APIView):
    def post(self, request):
        serializer = HealthInsuranceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HealthInsuranceUpdateView(APIView):
    def put(self, request, pk):
        health_insurance = get_object_or_404(HealthInsurance, pk=pk)
        serializer = HealthInsuranceSerializer(health_insurance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HealthInsuranceDeleteView(APIView):
    def delete(self, request, pk):
        health_insurance = get_object_or_404(HealthInsurance, pk=pk)
        health_insurance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class PatientCreateView(APIView):
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientUpdateView(APIView):
    def put(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientDeleteView(APIView):
    def delete(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PatientDetailView(APIView):
    def get(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
class PatientListView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)