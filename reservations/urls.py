from django.urls import path
from .views import (
    CancelReservationsView,
    RoomReservationsViewSet,
    UpdateReservationsView,
    GetRoomReservationsByIDView,
)

urlpatterns = [
    path("", RoomReservationsViewSet.as_view(), name="reservations"),
    path("<int:employees>", GetRoomReservationsByIDView.as_view(), name="reservations"),
    path("edit/<int:id>", UpdateReservationsView.as_view(), name="reservations_edit"),
    path(
        "cancel/<int:id>", CancelReservationsView.as_view(), name="reservations_cancel"
    ),
]
