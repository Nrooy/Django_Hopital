from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Appointment
from .serializers import AppointmentSerializer
from .filters import AppointmentFilter

class ListCreateAppointmentAPIView(ListCreateAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = [AllowAny]
    filterset_class = AppointmentFilter

class RetrieveUpdateDestroyAppointmentAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = [AllowAny]
