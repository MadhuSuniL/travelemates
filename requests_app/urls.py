from django.urls import path
from .views import AllRequests
urlpatterns = [
    path('get_reqs/',AllRequests.as_view())
]

