from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import *
urlpatterns = [
    path('login', LoginView.as_view()),
    path('register', TravelerRegisterView.as_view()),
    path('otp_verify', OTPVerificationView.as_view()),
    path('send_email', EmailSend.as_view()),
    path('details/', TravelerDetails.as_view()),
    path('update_name', UpdateName.as_view()),
    path('update_number', UpdateNumber.as_view()),
    path('update_profile', UpdateProfile.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]

