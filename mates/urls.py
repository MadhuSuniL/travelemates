from django.urls import path
from .views import *
urlpatterns = [
    path('get_mates/',AllMatesView.as_view()),
]
