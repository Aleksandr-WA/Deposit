from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_not_before_today(value):
    if value < timezone.now().date():
        raise ValidationError('Дата не может быть раньше текущей даты.')