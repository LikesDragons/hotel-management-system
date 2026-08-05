from django.db import models
from django.contrib.auth.models import User


class Guest(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="guest_profile"
    )

    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Staff(models.Model):
    DESIGNATIONS = [
        ("RECEPTIONIST", "Receptionist"),
        ("HOUSEKEEPING", "Housekeeping"),
        ("MANAGER", "Manager"),
        ("CHEF", "Chef"),
        ("SECURITY", "Security"),
        ("OTHER", "Other"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="staff_profile"
    )

    employee_id = models.CharField(max_length=20, unique=True)
    designation = models.CharField(
        max_length=20,
        choices=DESIGNATIONS
    )

    def __str__(self):
        return f"{self.employee_id} - {self.user.get_full_name() or self.user.username}"