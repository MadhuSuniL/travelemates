from rest_framework import serializers
from .models import Traveler


class TravelerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traveler
        fields = ['id','profile','name','phone_number','trips','mates','fans']
            