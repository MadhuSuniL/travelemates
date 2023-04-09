from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TripsData
from rest_framework.serializers import ModelSerializer
# Create your views here.

class Serialiser(ModelSerializer):
    class Meta:
        model = TripsData
        fields = '__all__'
        



class TripDataView(APIView):
    
    def get(self,request,contry=None):
        data = TripsData.objects.filter(contry=contry)
        data = Serialiser(data,many=True).data
        return Response(data,200)
            
            

            
            
            
            
