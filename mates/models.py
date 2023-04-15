from django.db import models
from travelers_app.models import Traveler
# Create your models here.

    
class TravelsMates(models.Model):
    traveler_var = models.ForeignKey(Traveler, on_delete=models.CASCADE, related_name='traveler_mates')
    mate_var = models.ForeignKey(Traveler, on_delete=models.CASCADE, related_name='mate_travelers')
