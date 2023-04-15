from django.urls import path
from .views import AllRequests
urlpatterns = [
    path('get_reqs/',AllRequests.as_view()),
    path('accept_reject/<int:pk>',AllRequests.as_view()),
    path('delete',AllRequests.as_view()),
]

