from django.db import models
from django.contrib.auth.models import User

class Ride(models.Model):
    pickup = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.pickup} to {self.destination} on {self.date}'
# models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Adjust max_length as needed

    def __str__(self):
        return self.user.username
