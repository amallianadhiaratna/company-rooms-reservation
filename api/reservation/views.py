from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import GetReservationSerializer, ReservationSerializer, UpdateReservationsSerializer
from api.models import RoomReservation


class RoomReservationsViewSet(generics.CreateAPIView):
    queryset = RoomReservation.objects.all()
    serializer_class = ReservationSerializer

class GetRoomReservationsView(generics.ListAPIView):
    queryset = RoomReservation.objects.all()
    serializer_class = GetReservationSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('employees')

class GetRoomReservationsByIDView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = RoomReservation.objects.all()
    # serializer_class = GetReservationSerializer

class UpdateReservationsView(generics.UpdateAPIView):
    queryset = RoomReservation.objects.all()
    serializer_class = UpdateReservationsSerializer