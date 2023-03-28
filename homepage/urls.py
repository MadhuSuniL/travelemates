from django.urls import path
from .views import *

urlpatterns = [
    path('trip_create',TripCreateView.as_view()),
    path('trip_get/',TripView.as_view()),
    path('trip_get_for_user/',TripView2.as_view()),
]