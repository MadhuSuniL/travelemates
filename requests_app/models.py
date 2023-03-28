from django.db import models
from travelers_app.models import Traveler
from homepage.models import Trip
# Create your models here.


class Request(models.Model):
    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip , on_delete=models.CASCADE)
    status = models.CharField(max_length=20,default='waiting')
    time = models.DateTimeField(auto_now_add=True)
    
    