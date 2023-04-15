from rest_framework.serializers import ModelSerializer
from travelers_app.models import Traveler
from homepage.models import Trip
from .models import Request
from rest_framework import serializers
from django.utils import timezone

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
        if minutes < 60:
            return f'{minutes} minutes ago'
        hours = minutes // 60
        if hours == 1:
            return '1 hour ago'
        return f'{hours} hours ago'




class TravelerSerializer(ModelSerializer):
    class Meta:
        model = Traveler
        fields = ['id','name','profile']
        
class TripSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = ['title','to_var']
        
class RequestSerializer(ModelSerializer):
    traveler = TravelerSerializer()
    trip = TripSerializer()
    time = RelativeDateTimeField()
    class Meta:
        model = Request
        exclude = ['status']
