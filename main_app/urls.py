"""django_first_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.views.generic import ListView

from main_app.models import TrainFlight, BusFlight
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bus/', ListView.as_view(queryset=BusFlight.objects.all(), template_name='main_app/bus.html')),
    path('train/', ListView.as_view(queryset=TrainFlight.objects.all(), template_name='main_app/train.html')),
]
