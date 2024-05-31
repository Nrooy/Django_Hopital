from djongo import models
from bson import ObjectId

class ObjectIdField(models.Field):
    description = "ObjectId"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 24
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'ObjectId'

    def get_prep_value(self, value):
        if not value:
            return None
        if isinstance(value, ObjectId):
            return str(value)
        return str(ObjectId(value))

    def from_db_value(self, value, expression, connection):
        if not value:
            return None
        if isinstance(value, ObjectId):
            return value
        return ObjectId(value)

class Clinic(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100) 
    description = models.TextField(default='')

    def __str__(self):
        return self.name


class ClinicRoom(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    room_number = models.CharField(max_length=10, unique=True)
    clinic = models.ForeignKey(Clinic, related_name='clinic_rooms', on_delete=models.CASCADE)

    def __str__(self):
        return f"Room {self.room_number} - Clinic: {self.clinic.name}"


class Bed(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    number = models.CharField(max_length=10)
    is_occupied = models.BooleanField(default=False)
    clinic_room = models.ForeignKey(ClinicRoom, related_name='beds', on_delete=models.CASCADE)

    def __str__(self):
        return f'Bed {self.number} - Room {self.clinic_room.room_number}'
