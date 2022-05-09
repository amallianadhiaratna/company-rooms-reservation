from ssl import create_default_context
from telnetlib import STATUS
from django.db import models
from .validators import validate_date_from, validate_date_to
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class Employee(User):
    division = models.CharField(max_length=120, blank=False, null=False)
    admin_access = models.BooleanField(default=False)
  
    def __str__(self):
        return self.username

class Room(models.Model):
    room        = models.CharField(max_length=120, blank=False, null=False) # max_length required
    description = models.CharField(max_length=120, blank=False, null=False) # max_length required
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.room

class RoomReservation(models.Model):
    title       = models.CharField(max_length=120, blank=False, null=False)
    room        = models.ForeignKey(Room, on_delete=models.CASCADE)
    # room        = models.CharField(max_length=120, blank=False, null=False) # max_length required
    employees   = models.ForeignKey(Employee, on_delete=models.CASCADE)
    book_at     = models.DateTimeField(auto_now_add=True)
    from_date   = models.DateTimeField(validators=[validate_date_from])
    to_date     = models.DateTimeField(validators=[validate_date_to])

    STATUS_VALID        = 0
    STATUS_CANCELLED    = 1
    STATUS_TYPES         = [
        (STATUS_VALID, "Valid"),
        (STATUS_CANCELLED, "Cancelled"),
    ]

    status = models.IntegerField(
        choices=STATUS_TYPES,
        default=STATUS_VALID, 
        blank=False, 
        null=False
    )
    def __str__(self):
        return f'Room Reservation title :{self.title}'

# class Employee(models.Model):
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     # account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  
#     def __str__(self):
#         return self.name

