from faulthandler import cancel_dump_traceback_later
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from authentication.models import Employee
from authentication.serializers import EmployeeSerializer


class ReservationsViewTest(APITestCase):
    def test_create_edit_reservations(self):
        username = "cupcake"
        email = "cupcake@foo.com"
        password = "password"
        division = "IT"

        # Create employee
        empolyee = Employee.objects.create_user(
            username=username, email=email, division=division, password=password
        )
        empolyee.save()

        # Login
        url = reverse("login")
        resp = self.client.post(
            url, {"email": email, "password": password}, format="json"
        )
        token = resp.data["tokens"]["access"]

        # Set API CLient with credentials
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

        # Create Room
        room = {"room": "Room 1", "description": "Ground Floor"}
        resp = client.post(reverse("rooms"), data=room, format="json")

        # Create Reservation
        room_id = resp.data["id"]
        employee_id = EmployeeSerializer(
            Employee.objects.get(username=username), many=False
        ).data["id"]
        reservation = {
            "title": "Meeting 1",
            "room": room_id,
            "employees": employee_id,
            "status": 1,
            "from_date": "2023-05-14T05:33:33.319Z",
            "to_date": "2023-05-14T07:33:33.319Z",
        }
        resp = client.post(reverse("reservations"), data=reservation, format="json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        reservation_id = resp.data["id"]

        # Try Delete Rooms
        resp = client.delete(reverse("rooms", args=[room_id]), format="json")
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        # Try Cancel Reservations
        resp = client.put(
            reverse("reservations_cancel", args=[reservation_id]),
            data={"status": 0},
            format="json",
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        # Try Unknown Cancel Reservations
        resp = client.put(
            reverse("reservations_cancel", args=[100]),
            data={"status": 0},
            format="json",
        )
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)

        # Try Edit Reservations
        edit_reservation = {
            "title": "New Meeting Title",
            "room": room_id,
            "status": 1,
            "from_date": "2023-05-14T05:33:33.319Z",
            "to_date": "2023-05-14T07:33:33.319Z",
        }
        resp = client.put(
            reverse("reservations_edit", args=[reservation_id]),
            data=edit_reservation,
            format="json",
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_create_reservations_with_same_room_and_time(self):
        username = "cupcake"
        email = "cupcake@foo.com"
        password = "password"
        division = "IT"

        # Create employee
        empolyee = Employee.objects.create_user(
            username=username, email=email, division=division, password=password
        )
        empolyee.save()

        # Login
        url = reverse("login")
        resp = self.client.post(
            url, {"email": email, "password": password}, format="json"
        )
        token = resp.data["tokens"]["access"]

        # Set API CLient with credentials
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

        # Create Room
        room = {"room": "Room 1", "description": "Ground Floor"}
        resp = client.post(reverse("rooms"), data=room, format="json")

        # Create Reservation
        room_id = resp.data["id"]
        employee_id = EmployeeSerializer(
            Employee.objects.get(username=username), many=False
        ).data["id"]
        reservation = {
            "title": "Meeting 1",
            "room": room_id,
            "employees": employee_id,
            "status": 1,
            "from_date": "2023-05-14T05:33:33.319Z",
            "to_date": "2023-05-14T07:33:33.319Z",
        }
        resp = client.post(reverse("reservations"), data=reservation, format="json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

         # Try Create Reservation for the same room and time
        room_id = resp.data["id"]
        employee_id = EmployeeSerializer(
            Employee.objects.get(username=username), many=False
        ).data["id"]
        reservation = {
            "title": "Meeting 1",
            "room": room_id,
            "employees": employee_id,
            "status": 1,
            "from_date": "2023-05-14T05:33:33.319Z",
            "to_date": "2023-05-14T07:33:33.319Z",
        }
        resp = client.post(reverse("reservations"), data=reservation, format="json")
        self.assertEqual(resp.data['error'][0], "The room is already reserved for your requested time range")
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)