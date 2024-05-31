from django.urls import path
from .views import MedicalRecordAPIView, MedicalRecordListAPIView

urlpatterns = [
    path('medical-record', MedicalRecordAPIView.as_view(), name='medical-record'),
    path('medical-records', MedicalRecordListAPIView.as_view(), name='medical-records'),
]