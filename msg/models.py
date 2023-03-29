from django.db import models
from travelers_app.models import Traveler
# Create your models here.


class Message(models.Model):
    sender = models.ForeignKey(Traveler, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(Traveler, on_delete=models.CASCADE, related_name='received_messages')
    message = models.CharField(max_length=1500)
    time = models.DateTimeField(auto_now_add=True)


    