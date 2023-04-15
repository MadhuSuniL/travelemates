from rest_framework.serializers import ModelSerializer
from travelers_app.models import Traveler
from homepage.models import Trip
from .models import Message
from django.utils import timezone
from rest_framework import serializers

class RelativeDateTimeField(serializers.DateTimeField):
    def to_representation(self, value):
        now = timezone.now()
        delta = now - value

        if delta.days >= 365:
            years = delta.days // 365
            if years == 1:
                return '1 year ago'
            return f'{years} years ago'

        if delta.days >= 30:
            months = delta.days // 30
            if months == 1:
                return '1 month ago'
            return f'{months} months ago'

        if delta.days >= 7:
            weeks = delta.days // 7
            if weeks == 1:
                return '1 week ago'
            return f'{weeks} weeks ago'

        if delta.days > 0:
            if delta.days == 1:
                return '1 day ago'
            return f'{delta.days} days ago'

        seconds = delta.seconds
        if seconds < 10:
            return 'just now'
        if seconds < 60:
            return f'{seconds} seconds ago'
        minutes = seconds // 60
        if minutes == 1:
            return '1 minute ago'
        return f'{minutes} minutes ago'

class TravelerSerializer(ModelSerializer):
    class Meta:
        model = Traveler
        fields = ['id','name','profile']
        
class MessageSerializer(ModelSerializer):
    sender = TravelerSerializer(read_only=True)
    receiver = TravelerSerializer(read_only=True)
    time = RelativeDateTimeField()
    class Meta:
        model = Message
        fields = '__all__'
        
        