from django.db import models


class Room(models.Model):
    room = models.CharField(max_length=120, blank=False, null=False)
    description = models.CharField(max_length=120, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.room
