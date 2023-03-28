from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from travelers_app.models import Traveler
from homepage.models import Trip
from .models import Request
from .serializers import *
# Create your views here.


class AllRequests(APIView):
    
    def get(self,request):
        id = request.user.id
        id = 22
        traveler = Traveler.objects.get(id=id)
        mytrips = Trip.objects.filter(traveler=traveler)
        mytrips_ids = []
        for mytrip in mytrips:
            mytrips_ids.append(mytrip.id)
            
        requests = Request.objects.filter(trip__id__in = mytrips_ids,status='waiting')
        
        data = RequestSerializer(requests,many=True).data
        
        return Response(data)
