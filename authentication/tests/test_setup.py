from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker

from authentication.models import Employee


class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.fake = Faker()

        self.user_data = {
            "email": self.fake.email(),
            "username": self.fake.email().split("@")[0],
            "password": self.fake.email(),
            "division": "IT",
        }

        self.user_data_incomplete = {
            # "username": self.fake.email().split("@")[0],
            "password": self.fake.email(),
            "division": "IT",
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()