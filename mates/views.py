from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TravelsMates
from travelers_app.models import Traveler
from .serializers import TravelsMateSerializer

class AllMatesView(APIView):
    
    def get(self,request):
        id = request.user.id
        id = 1
        traveler = Traveler.objects.get(id=id)
        
        mates = TravelsMates.objects.filter(traveler_var=traveler)
        data = TravelsMateSerializer(mates).data

        return Response(data,200)



