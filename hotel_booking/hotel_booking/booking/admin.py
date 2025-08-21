from django.contrib import admin
from .models import Room,Booking

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display=('number','room_type','price_per_night','is_available')
    list_filter=('room_type','is_available')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display=('guest_name','room','check_in','check_out')
    list_filter=('check_in','check_out')

