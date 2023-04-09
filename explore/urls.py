from django.urls import path
from .views import *
urlpatterns = [
     path('trips/<str:contry>',TripDataView.as_view())
     
]