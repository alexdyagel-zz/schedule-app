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
from django_filters.views import FilterView

from main_app.filters import BusFilter, TrainFilter
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bus/', FilterView.as_view(filterset_class=BusFilter, template_name='main_app/bus.html'), name="bus"),
    path('train/',
         FilterView.as_view(filterset_class=TrainFilter, template_name='main_app/train.html'), name="train"),
    path('json-example_bus/', views.json_example_bus, name='json_example'),
    path('json-example_bus/data/', views.chart_data_bus, name='chart_data'),
    path('json-example_train/', views.json_example_train, name='json_example'),
    path('json-example_train/data/', views.chart_data_train, name='chart_data')

]
