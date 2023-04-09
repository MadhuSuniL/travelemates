from django.db import models

# Create your models here.


class TripsData(models.Model):
    title = models.CharField(max_length = 200)
    image = models.CharField(max_length = 800)
    content = models.TextField()
    contry = models.CharField(max_length=200)
    
