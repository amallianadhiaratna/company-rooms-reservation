from django.db import models
from authentication.models import Employee
from rooms.models import Room
from .validators import validate_date_from, validate_date_to


class Reservation(models.Model):
    title = models.CharField(max_length=120, blank=False, null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # room        = models.CharField(max_length=120, blank=False, null=False) # max_length required
    employees = models.ForeignKey(Employee, on_delete=models.CASCADE)
    book_at = models.DateTimeField(auto_now_add=True)
    from_date = models.DateTimeField(validators=[validate_date_from])
    to_date = models.DateTimeField(validators=[validate_date_to])

    STATUS_VALID = 1
    STATUS_CANCELLED = 0
    STATUS_TYPES = [
        (STATUS_VALID, "Valid"),
        (STATUS_CANCELLED, "Cancelled"),
    ]

    status = models.IntegerField(
        choices=STATUS_TYPES, default=STATUS_VALID, blank=False, null=False
    )

    def __str__(self):
        return self.title
