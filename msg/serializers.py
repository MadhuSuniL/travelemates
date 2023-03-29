from rest_framework.serializers import ModelSerializer
from travelers_app.models import Traveler
from homepage.models import Trip
from .models import Message

class TravelerSerializer(ModelSerializer):
    class Meta:
        model = Traveler
        fields = ['id','name','profile']
        
class MessageSerializer(ModelSerializer):
    sender = TravelerSerializer(read_only=True)
    receiver = TravelerSerializer(read_only=True)
    class Meta:
        model = Message
        fields = '__all__'
        