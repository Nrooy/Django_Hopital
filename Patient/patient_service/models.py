# from django.db import models
from djongo import models
class HealthInsurance(models.Model):
    patient_id = models.CharField(max_length=7, primary_key=True)
    insurance_number = models.CharField(max_length=50, unique=True)
    provider_name = models.CharField(max_length=100)
    policy_start_date = models.DateField()
    policy_end_date = models.DateField()
    coverage_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Insurance {self.insurance_number} - {self.provider_name}'
class Patient(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    health_insurance = models.CharField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    health_insurance = models.ForeignKey(HealthInsurance, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'




