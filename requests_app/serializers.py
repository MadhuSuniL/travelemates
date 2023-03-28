from rest_framework.serializers import ModelSerializer
from travelers_app.models import Traveler
from homepage.models import Trip
from .models import Request

class TravelerSerializer(ModelSerializer):
    class Meta:
        model = Traveler
        fields = ['id','name','profile']
        
class TripSerializer(ModelSerializer):
    traveler = TravelerSerializer(read_only=True)
    class Meta:
        model = Trip
        fields = ['title','to']
        
class RequestSerializer(ModelSerializer):
    traveler = TravelerSerializer(read_only=True)
    trip = TripSerializer
    class Meta:
        model = Request
        exclude = ['status']
