from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from dateutil.parser import parse
from django.utils import timezone
from api.models import Room, RoomReservation
from api.reservation.serializers import ReservationSerializer
from .serializers import RoomSerializer

class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    http_request_methods = ['get', 'post', 'delete', 'put']

    def delete(self, request, pk):
        room = self.get_object()
        reservations = ReservationSerializer(RoomReservation.objects.all().filter(
            room=room.room, status=0), many=True).data

        if reservations:
            for reservation in reservations:
                if parse(reservation['from_date']).astimezone(timezone.get_current_timezone()) <= timezone.localtime(timezone.now()) <= parse(reservation['to_date']).astimezone(timezone.get_current_timezone()):
                    return Response({'status': "Cannot delete this room, there's on-going reservation"}, status=status.HTTP_400_BAD_REQUEST)
        room.delete()
        return Response({'status': "Meeting Room was successfully deleted"}, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save()
