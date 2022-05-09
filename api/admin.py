from django.contrib import admin
from .models import RoomReservation, Room, Employee

admin.site.register(Room)
admin.site.register(RoomReservation)
admin.site.register(Employee)