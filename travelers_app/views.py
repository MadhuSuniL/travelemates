from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Traveler
from .email_send import EmailThread
from django.conf import settings
# Create your views here.


# def test(r):
#     email = EmailThread('Subject', '<h1>487676</h1>', settings.EMAIL_HOST_USER, ['bagammagarimadhu@gmail.com'])
#     email.start()



class TravelerRegisterView(APIView):
    
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
        # try:
        traveler = Traveler.objects.create_user(email=email,password=email[::-1],phone_number=whasapp_no,profile=profile,mother_tounge=language)
        #except:
         #   return Response('Email already exist!',400)
        
        
        return Response('Registration is completed!',200)
    
    
class OTPVerificationView(APIView):
    
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
        