from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date


def no_future_date(value):
    if value > date.today():
        raise ValidationError('Date cannot be in the future')
