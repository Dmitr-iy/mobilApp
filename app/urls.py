from django.urls import path
from .views import DoctorListCreateView, LocationListCreateView

urlpatterns = [
    path('doctor/', DoctorListCreateView.as_view(), name='doctor_list_create'),
    path('', LocationListCreateView.as_view(), name='location_list_create'),
]


