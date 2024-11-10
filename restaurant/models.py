from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reservations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField(auto_now_add=True)
    people = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=15)
    message = models.TextField()

    class Meta:
        ordering = ["-date_and_time"]

    def __str__(self):
        return f"{self.user} made a reservation for {self.people} guests "

    

    
