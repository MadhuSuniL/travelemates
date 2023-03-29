from django.urls import path
from .views import *
urlpatterns = [
    path('get_chat/',AllMessages.as_view()),
    path('get_msg/<int:id>',IdMsg.as_view()),
]