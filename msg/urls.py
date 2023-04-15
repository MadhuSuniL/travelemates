from django.urls import path
from .views import *
urlpatterns = [
    path('get_msgs/',AllMessages.as_view()),
    path('recv_msg',AllMessages.as_view()),
]
