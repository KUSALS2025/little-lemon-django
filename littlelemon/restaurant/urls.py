
from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.bookings, name='bookings'),
    path('available-times/', views.available_times, name='available_times'),
]
