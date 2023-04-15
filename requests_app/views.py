from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from travelers_app.models import Traveler
from homepage.models import Trip
from .models import Request
from .serializers import *
from mates.models import TravelsMates


class AllRequests(APIView):

    def get(self,request):
        id = request.user.id
        id = 1
        traveler = Traveler.objects.get(id=id)
        mytrips = Trip.objects.filter(traveler=traveler)
        mytrips_ids = []
        for mytrip in mytrips:
            mytrips_ids.append(mytrip.id)
            
        requests = Request.objects.filter(trip__id__in = mytrips_ids,status='waiting')
        
        data = RequestSerializer(requests,many=True).data
        
        return Response(data)

    #accepting-rejecting 
    def put(self,request,pk=None):
        id = 1
        traveler = Traveler.objects.get(id=id)
        action = request.data['action']
        request_var = Request.objects.get(id=pk)
        if action == 'accept':
            print('a')
            request_var.status = action
            TravelsMates.objects.create(traveler_var=traveler,mate_var=request_var.traveler)            
            TravelsMates.objects.create(traveler_var=request_var.traveler,mate_var=traveler)            
            request_var.save()
        else:
            print('d')
            request_var.delete()
                
        return Response('None',200)
    def delete(self,request,pk=None):
        id = 1
        traveler = Traveler.objects.get(id=id)
        request_var = Request.objects.filter(traveler=traveler)
        request_var.delete()
        return Response('None',200)

                

