from django.shortcuts import render
from .models import Message
from rest_framework.response import Response
from travelers_app.models import Traveler
from rest_framework.views import APIView
from .serializers import MessageSerializer
# Create your views here.


class AllMessages(APIView):

    def get(self,request):
        # id = 1
        id = request.user.id
        traveler = Traveler.objects.get(id=id)
        mesgs = Message.objects.filter(receiver = traveler)
        data = MessageSerializer(mesgs,many=True).data
        
        return Response(data)

    def post(self,request):
        # id = 1
        id = request.user.id
        receiver_id = request.data['receiver_id']
        sender = Traveler.objects.get(id=id)
        receiver = Traveler.objects.get(id=id)
        message = request.data['message']
        msg = Message.objects.create(sender=sender,receiver=receiver,message=message)

        return Response('OK',200)


class IdMsg(APIView):

    def get(self,request,id=None):
        id = 1
        mesgs = Message.objects.filter(id = id)
        print(',,,,,,,,,,,,,',mesgs[0].message)
        data = MessageSerializer(mesgs,many=True).data

        return Response(data)
