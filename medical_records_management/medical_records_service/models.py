from djongo import models


class Prescription(models.Model):
    _id = models.ObjectIdField()
    medication_id = models.CharField(max_length=24)
    name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.dosage}, {self.frequency})"


class MedicalRecord(models.Model):
    _id = models.ObjectIdField()
    patient_id = models.CharField(max_length=24)
    doctor_id = models.CharField(max_length=24)
    visit_date = models.DateField()
    diagnosis = models.TextField()
    prescriptions = models.ArrayField(model_container=Prescription)
    doctor_notes = models.TextField()