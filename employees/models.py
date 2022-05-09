from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Employees(User):
    division = models.CharField(max_length=120, blank=False, null=False)
    admin_access = models.BooleanField(default=False)
  
    def __str__(self):
        return self.username
