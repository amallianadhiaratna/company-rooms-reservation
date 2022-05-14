from django.utils import timezone
from rest_framework import serializers
from authentication.serializers import EmployeeSerializer
from .models import Reservation


class GetReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            "id",
            "title",
            "room",
            "employees",
            "status",
            "from_date",
            "to_date",
            "status",
        )


class EditReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            "title",
            "room",
            "status",
            "from_date",
            "to_date",
        )
        extra_kwargs = {"title": {"min_length": 8}}


class CancelReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            'status',
        )
    # def save(self, **kwargs):
    #     if reservation.status is 0:
    #         reservation.status = 1
    #         reservation.save()
    #         return ReservationSerializer(reservation)
    #     raise serializers.ValidationError(
    #             {"error": "Reservation is already cancelled"})

class ReservationSerializer(serializers.ModelSerializer):
    # status = serializers.SerializerMethodField()

    class Meta:

        model = Reservation
        fields = (
            "id",
            "title",
            "room",
            "employees",
            "status",
            "from_date",
            "to_date",
            "book_at",
        )
        extra_kwargs = {"title": {"min_length": 8}}
        # read_only_fields = ('status')

    # def get_status(self, obj):
    #     return obj.get_status_display()

    def validate(self, data):
        print("validate")
        # We convert the provided date & time to our local server timezone (UTC+3)

        wanted_date_from = data["from_date"].astimezone(timezone.get_current_timezone())
        wanted_date_to = data["to_date"].astimezone(timezone.get_current_timezone())

        # Check if the reservation starting time isn't greater than reservation ending time.
        if wanted_date_to <= wanted_date_from:
            raise serializers.ValidationError(
                "Meeting could not end earlier than it starts"
            )

        # Check if there are any other VALID reservations by that time range.
        reservations = Reservation.objects.all().filter(room=data["room"], status=1)
        if reservations:
            for reservation in reservations:
                from_date = reservation.from_date.astimezone(
                    timezone.get_current_timezone()
                )
                to_date = reservation.to_date.astimezone(
                    timezone.get_current_timezone()
                )
                if (
                    from_date <= wanted_date_from <= to_date
                    or from_date <= wanted_date_to <= to_date
                ):
                    raise serializers.ValidationError(
                        "The room is already reserved for your requested time range"
                    )
        return data
