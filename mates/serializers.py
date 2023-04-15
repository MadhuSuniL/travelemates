from rest_framework import serializers
from travelers_app.models import Traveler
from .models import TravelsMates



class TravelerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traveler
        fields = ['id','name','profile']
        
        
class TravelsMateSerializer(serializers.ModelSerializer):
    traveler_var = TravelerSerializer(read_only=True)
    class Meta:
        model = TravelsMates
        fields = '__all__'
        