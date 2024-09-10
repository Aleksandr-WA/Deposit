from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Deposit(models.Model):
    date = models.DateField()
    periods = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(60)]
    )
    amount = models.IntegerField(
        validators=[MinValueValidator(10_000), MaxValueValidator(3_000_000)]
    )
    rate = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(8)])
    calculated_value = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
