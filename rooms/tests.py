from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from authentication.models import Employee


# models test
class RoomViewTest(APITestCase):
    """
    This is the test for room views
    """

    def test_get_room(self):
        url = reverse("login")
        employee = Employee.objects.create_user(
            username="cupcake",
            email="cupcake@foo.com",
            division="IT",
            password="password",
        )
        employee.save()

        resp = self.client.post(
            url, {"email": "cupcake@foo.com", "password": "password"}, format="json"
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        token = resp.data["tokens"]["access"]

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION="Bearer wrong_token")

        # Get Room with the wrong credentials
        resp = client.get(reverse("rooms"), data={"format": "json"})
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

        # Get Room with the right credentials
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        resp = client.get(reverse("rooms"), data={"format": "json"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_create_delete_room(self):
        url = reverse("login")
        employee = Employee.objects.create_user(
            username="cupcake",
            email="cupcake@foo.com",
            division="IT",
            password="password",
        )
        employee.save()

        resp = self.client.post(
            url, {"email": "cupcake@foo.com", "password": "password"}, format="json"
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        token = resp.data["tokens"]["access"]

        data = {"room": "Room 1", "description": "Ground Floor"}
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f"Bearer wrong_token")
        resp = client.post(reverse("rooms"), data=data, format="json")
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

        # Create Room
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        resp = client.post(reverse("rooms"), data=data, format="json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        # Delete Room
        room_id = resp.data["id"]
        resp = client.delete(reverse("rooms", args=[room_id]), format="json")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
