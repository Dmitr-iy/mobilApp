from django.urls import path
from .views import DoctorListCreateView, LocationListCreateView

urlpatterns = [
    path('doctor/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('', LocationListCreateView.as_view(), name='location-list-create'),
]


# from django.urls import path
# from .views import LocationCreateView
#
# urlpatterns = [
#     path('', LocationCreateView.as_view(), name='location-create'),
# ]


# from django.urls import path
# from .views import SaveLocationView
#
# app_name = 'app'
#
# urlpatterns = [
#     path('save-location/', SaveLocationView.as_view(), name='save_location'),
# ]
#


# from django.urls import include, path
# from rest_framework import routers
#
# from app import views
#
# router = routers.DefaultRouter()
# router.register(r'loc', views.LocationViewset)
# # router.register(r'doc', views.DoctorViewset)
#
# urlpatterns = [
#      path('', include(router.urls)),
# ]
