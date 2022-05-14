from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from dateutil.parser import parse
from django.utils import timezone
import datetime
import logging
from reservations.serializers import ReservationSerializer
from reservations.models import Reservation
from .models import Room
from .serializers import RoomSerializer


logger = logging.getLogger(__name__)

class RoomListAPIView(ListCreateAPIView):
    logger.warning(f'{str(datetime.datetime.now())} : Request to access /rooms')
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class RoomDetailAPIView(RetrieveUpdateDestroyAPIView):
    logger.warning(f'{str(datetime.datetime.now())} : Request to access /rooms/id')
    serializer_class = RoomSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Room.objects.all()
    lookup_field = "id"

    def delete(self, request, *args, **kwargs):
        logger.warning(f'{str(datetime.datetime.now())} : Request to delete rooms on /rooms/id')
        id = kwargs["id"]
        room = self.get_object()
        reservations = ReservationSerializer(
            Reservation.objects.all().filter(room=id, status=1), many=True
        ).data

        if reservations:
            for reservation in reservations:
                from_date = parse(reservation["from_date"]).astimezone(
                    timezone.get_current_timezone()
                )
                to_date = parse(reservation["to_date"]).astimezone(
                    timezone.get_current_timezone()
                )
                current_time = timezone.localtime(timezone.now())

                if from_date >= current_time or  current_time <= to_date:
                    return Response(
                        {
                            "status": "Cannot delete this room, there's on-going reservation"
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
        room.delete()
        return Response(
            {"status": "Meeting Room was successfully deleted"},
            status=status.HTTP_200_OK,
        )
