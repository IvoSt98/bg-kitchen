from django.db import models
from django.contrib.auth.models import User


# Create your models here.

""" 
The Reservations model represents a booking made by a user, including details like 
the user making the reservation, the reservation date and time, the number of guests, 
the user's contact phone number, any special message, and whether the reservation is approved. 
The reservations are ordered by the most recent first, and the model's string representation 
returns a description of the reservation with the user's name and number of guests.
"""
class Reservations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField()
    people = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    
    

    class Meta:
        ordering = ["-date_and_time"]

    def __str__(self):
        return f"{self.user} made a reservation for {self.people} guests "