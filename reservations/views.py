from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Reservation
from .permissions import IsOwner
from .serializers import (
    CancelReservationsSerializer,
    ReservationSerializer,
    EditReservationsSerializer,
)


class RoomReservationsViewSet(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (permissions.IsAuthenticated,)


class GetRoomReservationsByIDView(generics.ListAPIView):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            reservation_data = Reservation.objects.all().filter(employees=kwargs["employees"]).values()
            return Response(
                {
                    "status": "Successfully get the reservations",
                    "reservation": list(reservation_data),
                },
                status=status.HTTP_200_OK,
            )
        except Reservation.DoesNotExist:
            return Response(
                {"status": f"Cannot found a valid reservations by id : {kwargs['id']}"},
                status=status.HTTP_404_NOT_FOUND,
            )   


class UpdateReservationsView(generics.UpdateAPIView):
    lookup_field = "id"
    queryset = Reservation.objects.all()
    serializer_class = EditReservationsSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)


class CancelReservationsView(generics.UpdateAPIView):
    lookup_field = "id"
    queryset = Reservation.objects.all()
    serializer_class = CancelReservationsSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)