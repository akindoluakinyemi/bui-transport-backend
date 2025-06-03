from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model to support roles
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('organizer', 'Transport Organizer'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    def __str__(self):
        return self.username

# Transport organizer profile linked to the custom user
class TransportOrganizer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    contact_info = models.TextField()
    approved = models.BooleanField(default=False)

# Vehicles listed by organizers
class Vehicle(models.Model):
    organizer = models.ForeignKey(TransportOrganizer, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=50)  # cab, sienna, bus, etc.
    capacity = models.IntegerField()
    features = models.TextField(blank=True)

# Bookings by students
class Booking(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    transport_option = models.ForeignKey('TransportOption', on_delete=models.CASCADE)
    trip_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    PAYMENT_CHOICES = [
        ('online', 'Online'),
        ('cash', 'Cash'),
    ]
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='cash')
    is_paid = models.BooleanField(default=False)
    payment_reference = models.CharField(max_length=255, blank=True, null=True)

# Optional if you're using it separately
class TransportOption(models.Model):
    VEHICLE_TYPES = [
        ('cab', 'Cab'),
        ('sienna', 'Sienna'),
        ('bus', 'Bus'),
    ]
    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'organizer'})
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    comfort_features = models.TextField(blank=True)
    available_dates = models.TextField(help_text="Comma-separated list of dates (e.g. 2024-05-01,2024-05-02)")
    pickup_point = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    approved = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.vehicle_type} by {self.organizer}"
