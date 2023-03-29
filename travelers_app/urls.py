from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import *
urlpatterns = [
    path('login', LoginView.as_view()),
    path('register', TravelerRegisterView.as_view()),
    path('otp_verify', OTPVerificationView.as_view()),
    path('send_email', EmailSend.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]