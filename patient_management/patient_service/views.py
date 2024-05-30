from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    @action(detail=True, methods=["get"])
    def profile(self, request, pk=None):
        patient = self.get_object()
        serializer = self.get_serializer(patient)
        return Response(serializer.data)

    @action(detail=True, methods=["put"])
    def update_profile(self, request, pk=None):
        patient = self.get_object()
        serializer = self.get_serializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["delete"])
    def delete_profile(self, request, pk=None):
        patient = self.get_object()
        patient.delete()
        return Response(
            {"message": "Patient profile deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )

    @action(detail=True, methods=["get"])
    def history(self, request, pk=None):
        patient = self.get_object()
        history = patient.medical_history
        serializer = self.get_serializer(history, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["put"])
    def update_history(self, request, pk=None):
        patient = self.get_object()
        history_serializer = MedicalHistorySerializer(
            data=request.data.get("medical_history"), many=True
        )
        if history_serializer.is_valid():
            patient.medical_history = history_serializer.validated_data
            patient.save()
            return Response(history_serializer.data)
        return Response(history_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
