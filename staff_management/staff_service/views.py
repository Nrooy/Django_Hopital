from django.shortcuts import render
from rest_framework import viewsets
from .models import Staff, Attendance, Payroll
from .serializers import StaffSerializer, AttendanceSerializer, PayrollSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    @action(detail=True, methods=['get'])
    def profile(self, request, pk=None):
        staff = self.get_object()
        serializer = self.get_serializer(staff)
        return Response(serializer.data)

# class AttendanceViewSet(viewsets.ModelViewSet):
#     queryset = Attendance.objects.all()
#     serializer_class = AttendanceSerializer
#
#     @action(detail=True, methods=['get'])
#     def attendance(self, request, pk=None):
#         attendance = self.get_object()
#         serializer = self.get_serializer(attendance)
#         return Response(serializer.data)

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    @action(detail=False, methods=['get'], url_path='list/(?P<pk>[^/.]+)')
    def staff_attendance(self, request, pk=None):
        # Find the staff member with the given pk
        staff = get_object_or_404(Staff, pk=pk)
        # Filter the attendance records for this staff member
        attendances = Attendance.objects.filter(staff=staff)
        # Serialize the attendance records
        serializer = AttendanceSerializer(attendances, many=True)
        return Response(serializer.data)

class PayrollViewSet(viewsets.ModelViewSet):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer

    @action(detail=False, methods=['get'], url_path='detail/(?P<pk>[^/.]+)')
    def payroll(self, request, pk=None):
        staff = Staff.objects.get(pk=pk)
        attendances = Attendance.objects.filter(staff=staff, status='Present').count()
        hourly_rate = 1000
        total_salary = attendances * hourly_rate

        payroll_data = {
            'staff': staff.id,
            'attendances': attendances,
            'hourly_rate': hourly_rate,
            'total_salary': total_salary,
        }

        return Response(payroll_data)
