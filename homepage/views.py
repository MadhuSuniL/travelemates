from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from .models import Trip
from rest_framework.generics import GenericAPIView , ListAPIView, CreateAPIView

# Create your views here.


class TripView(ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripView2(ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get(self,request):
        # id = request.user.id
        id = 22
        trips = self.queryset.filter(traveler__id = id)
        data = self.serializer_class(trips,many=True).data
        return Response(data,200)

class TripCreateView(CreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripCreateSerializer
    
    def post(self,request):
        id = 22
        #id = request.user.id
        title = request.data.get('title',None)
        from_ = request.data.get('from_var',None)
        to_ = request.data.get('to_var',None)
        date = request.data.get('date',None)
        trip_for = request.data.get('trip_for',None)
        traveler = Traveler.objects.get(id=id)
        
        if title == None or from_ == None or to_ == None or date == None or trip_for == None:
            return Response('Check',403) 
            
        trip = Trip.objects.create(traveler=traveler,from_var=from_,to_var=to_,date=date,trip_for=trip_for,title=title)

        res = Response(trip,200)
        return res
    
    
    