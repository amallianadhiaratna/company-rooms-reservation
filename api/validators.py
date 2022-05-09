from django.core.exceptions import ValidationError
from dateutil.parser import parse
from django.utils import timezone


def validate_date_from(date):
    if timezone.localtime(timezone.now()) > date.astimezone(timezone.get_current_timezone()):
        raise ValidationError(
            "Meeting could not start earlier than the current time")
    return date


def validate_date_to(date):
    if timezone.localtime(timezone.now()) > date.astimezone(timezone.get_current_timezone()):
        raise ValidationError(
            "Meeting could not end earlier than the current time")
    return date