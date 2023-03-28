from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from travelers_app.models import Traveler
from .models import Trip


class TravelerSerializer(ModelSerializer):
    class Meta:
        model = Traveler
        fields = ['name','profile']
        
        
class TripSerializer(ModelSerializer):
    traveler = TravelerSerializer(read_only=True)
    time = serializers.CharField(read_only = True)
    class Meta:
        model = Trip
        fields = '__all__'

        
class TripCreateSerializer(ModelSerializer):
    time = serializers.CharField(read_only = True)
    class Meta:
        model = Trip
        fields = '__all__'
        
        
