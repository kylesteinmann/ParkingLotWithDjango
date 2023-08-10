from django.urls import path
from parkingSpots import views

urlpatterns = [
    path('', views.index, name='index'),
]
