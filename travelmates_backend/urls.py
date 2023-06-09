"""travelmates_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from travelers_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('t', test),
    path('travelers/',include('travelers_app.urls')),
    path('trips/',include('homepage.urls')),
    path('requests/',include('requests_app.urls')),
    path('messages/',include('msg.urls')),
    path('explore/',include('explore.urls')),
    path('travelmates/',include('mates.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
    