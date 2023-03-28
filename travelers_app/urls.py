from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import *
urlpatterns = [
    path('login', LoginView.as_view()),
    path('register', TravelerRegisterView.as_view()),
    path('otp_verify', OTPVerificationView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]