from djongo import models
from django.utils import timezone


class MedicalHistory(models.Model):
    date = models.DateField()
    diagnosis = models.CharField(max_length=255)
    treatment = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    medical_history = models.ArrayField(model_container=MedicalHistory)
    date_registered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
