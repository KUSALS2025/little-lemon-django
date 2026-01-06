
from django.shortcuts import render
from django.http import JsonResponse
from .models import Booking
from datetime import time

def bookings(request):
    return render(request, 'bookings.html')

def available_times(request):
    date = request.GET.get('date')
    booked = Booking.objects.filter(booking_date=date).values_list('booking_time', flat=True)

    all_times = [
        time(10,0), time(11,0), time(12,0),
        time(13,0), time(18,0), time(19,0), time(20,0)
    ]

    available = [t.strftime('%H:%M') for t in all_times if t not in booked]
    return JsonResponse({'available_times': available})
