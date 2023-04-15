from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from .models import Trip
from rest_framework.generics import GenericAPIView , ListAPIView, CreateAPIView

# Create your views here.


class TripView(ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    
    def post(self,request):
        title = request.data.get('title')
        from_ = request.data.get('from')
        to_ = request.data.get('to')
        trip_for = request.data.get('trip_for')
        date = request.data.get('date')
        
        trips = Trip.objects.all()
        
        if title != '':
            trips = trips.filter(title__contains = title)
        
        if from_ != '':
            trips = trips.filter(from_var__contains = from_)

        if to_ != '':
            trips = trips.filter(to_var__contains = to_)
            
        if trip_for != 'all':
            trips = trips.filter(trip_for = trip_for)
            
        if date != '':
            trips = trips.filter(date__gte = date)
            
        data = self.serializer_class(trips,many=True).data
        # print(data)
        return Response(data,200)



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
            return Response('Check',400) 
            
        trip = Trip.objects.create(traveler=traveler,from_var=from_,to_var=to_,date=date,trip_for=trip_for,title=title)
        data = TripSerializer(trip).data
        res = Response(data,200)
        return res
    
    
    