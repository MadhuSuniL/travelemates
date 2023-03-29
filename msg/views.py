from django.shortcuts import render
from .models import Message
from rest_framework.response import Response
from travelers_app.models import Traveler
from rest_framework.views import APIView
from .serializers import MessageSerializer
# Create your views here.


class AllMessages(APIView):

    def get(self,request):
        id = request.user.id
        id = 22
        traveler = Traveler.objects.get(id=id)
        mesgs = Message.objects.filter(sender = traveler) | Message.objects.filter(receiver = traveler)
        data = MessageSerializer(mesgs,many=True).data
        
        return Response(data)


class IdMsg(APIView):

    def get(self,request,id=None):
        id = 1
        mesgs = Message.objects.filter(id = id)
        print(',,,,,,,,,,,,,',mesgs[0].message)
        data = MessageSerializer(mesgs,many=True).data

        return Response(data)
