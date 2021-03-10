from django.urls import path
from . import views

urlpatterns = [
    path('nail', views.get_nail_services, name='nail_services'),
    path('massage', views.get_tanning_services, name='tanning_services'),
]