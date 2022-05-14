from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class EmployeeManager(BaseUserManager):
    def create_user(self, username, email, division, password=None):
        if username is None:
            raise TypeError("Employee should have a username")
        if email is None:
            raise TypeError("Employee should have a Email")

        user = self.model(
            username=username, email=self.normalize_email(email), division=division
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError("Password should not be none")

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class Employee(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    division = models.CharField(max_length=120)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = EmployeeManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}
