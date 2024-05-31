from django.db import models

class Pharmaceutical(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    expiry_date = models.DateField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class MedicalSupply(models.Model):
    name = models.CharField(max_length=255)
    supplier = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name