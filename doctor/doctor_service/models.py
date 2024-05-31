from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class Specialization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Doctor(models.Model):
    userId = models.IntegerField()
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, related_name='doctors')
    license_number = models.CharField(max_length=50, unique=True)
    specialization = models.ForeignKey(
        Specialization, on_delete=models.CASCADE, related_name='doctors')
    years_of_experience = models.IntegerField()
    qualifications = models.CharField(max_length=255)
    biography = models.TextField()

    def __str__(self):
        return f"Dr."


class Schedule(models.Model):
    DAYS_OF_WEEK = [
        (2, 'Thứ Hai'),
        (3, 'Thứ Ba'),
        (4, 'Thứ Tư'),
        (5, 'Thứ Năm'),
        (6, 'Thứ Sáu'),
        (7, 'Thứ Bảy'),
        (8, 'Chủ Nhật'),
    ]

    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='schedules')
    day_of_week = models.IntegerField(choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        day_str = dict(self.DAYS_OF_WEEK)[self.day_of_week]
        return f"{self.doctor} {day_str} từ {self.start_time} đến {self.end_time}"

    class Meta:
        unique_together = [['doctor', 'day_of_week', 'start_time', 'end_time']]


class Review(models.Model):
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='reviews')
    patientId = models.IntegerField()
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    comment = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review on {self.doctor}"
