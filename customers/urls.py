from django.contrib import admin
from django.urls import path,include
from .views import SegmentedCustomers

urlpatterns = [
    path('home',SegmentedCustomers),
]