from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .validators import validate_not_before_today


class Deposit(models.Model):
    date = models.DateField(validators=[validate_not_before_today])
    periods = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(60)])
    amount = models.IntegerField(validators=[MinValueValidator(10_000), MaxValueValidator(3_000_000)])
    rate = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(8)])
    calculated_value = models.JSONField(null=True, blank=True)








