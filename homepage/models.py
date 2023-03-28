from datetime import datetime
from django.db import models
from travelers_app.models import Traveler
# Create your models here.

class Trip(models.Model):
    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    from_var = models.CharField(max_length=100)
    to_var = models.CharField(max_length=100)
    trip_for = models.CharField(max_length=100)
    date = models.DateField()
    remaining_time = models.CharField(max_length=100)
    
    def save(self,*args, **kwargs):
        timer = self.date - datetime.now().date()
        self.remaining_time = f'{timer.days} days to go'
        super().save(*args, **kwargs)
        