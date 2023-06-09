from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Traveler
from .email_send import EmailThread
from django.conf import settings
from .serializers import TravelerDetailsSerializer
# Create your views here.


# def test(r):
#     email = EmailThread('Subject', '<h1>487676</h1>', settings.EMAIL_HOST_USER, ['bagammagarimadhu@gmail.com'])
#     email.start()



class TravelerRegisterView(APIView):
    authentication_classes =[]
    
    def post(self,request):
        email = request.data['email']
        name = request.data['name']
        otp = request.data['otp']
        language = request.data['language']
        profile = request.data.get('profile',None)
        whasapp_no = request.data['number']
        
        # otp sending to email
        email_ = EmailThread('Subject', str(otp), settings.EMAIL_HOST_USER, [email,])
        email_.start()

        #creating objs
        try:
            traveler = Traveler.objects.create_user(email=email,password=email[::-1],phone_number=whasapp_no,profile=profile,mother_tounge=language)
        except:
            return Response('Email already exist!',400)
        
        
        return Response('Registration is completed!',200)
    
    
class OTPVerificationView(APIView):
    authentication_classes =[]
    permission_classes = []
    
    def post(self,request):
        email = request.data['email']
        traveler = Traveler.objects.get(email=email)
        
        if not traveler.otp_verifyed:
             traveler.otp_verifyed = True
             traveler.save()
             
        refresh_token = RefreshToken.for_user(traveler)

        data = {
            'refresh':str(refresh_token),
            'access':str(refresh_token.access_token)
        }
        return Response(data,200)
        
class LoginView(APIView):
    authentication_classes =[]
    permission_classes = []
    
    def post(self,request):
        email = request.data['email']
        print('fffffffffff',email)
        traveler = Traveler.objects.get(email=email)
        
        refresh_token = RefreshToken.for_user(traveler)

        data = {
            'refresh':str(refresh_token),
            'access':str(refresh_token.access_token)
        }
        return Response(data,200)
    

class UpdateProfile(APIView):
    
    def put(self,request):
        id = request.user.id
        profile = request.data['profile']
        print(profile,type(profile))
        traveler = Traveler.objects.get(id=id)
        # profile = Traveler.objects.get(email=traveler.email)
        traveler.profile = profile
        traveler.save()
        return Response('Success!',200)
        
class UpdateName(APIView):
    
    def put(self,request):
        id = request.user.id
        name = request.data['name']
        traveler = Traveler.objects.get(id=id)
        # profile = Traveler.objects.get(email=traveler.email)
        traveler.name = name
        traveler.save()
        return Response('Success!',200)
    
class UpdateNumber(APIView):
    
    def put(self,request):
        id = request.user.id
        number = request.data['number']
        traveler = Traveler.objects.get(id=id)
        # profile = Traveler.objects.get(email=traveler.email)
        traveler.phone_number = number
        traveler.save()
        return Response('Success!',200)
        
        
class TravelerDetails(RetrieveAPIView):
    serializer_class = TravelerDetailsSerializer
    queryset = Traveler.objects.all()
    
    def get(self,request):
        id = 22 
        id = request.user.id
        traveler = Traveler.objects.get(id=id)
        data = self.serializer_class(traveler).data 
        return Response(data,200)      
        

class EmailSend(APIView):
    authentication_classes =[]
    permission_classes = []
    def post(self,request):
        email = request.data['email']
        otp = request.data['otp']
        try:
            Traveler.objects.get(email=email)
            email_ = EmailThread('Subject', str(otp), settings.EMAIL_HOST_USER, [email,])
            email_.start()
            return Response('done',200)
        except:
            return Response('User Not Found!',404)
        