from datetime import datetime
from rest_framework import serializers
from .models import Deposit


class DateFormatField(serializers.Field):
    def to_representation(self, value):
        if value:
            return value.strftime("%d.%m.%Y")
        return ""

    def to_internal_value(self, data):
        date_now = datetime.today().date()

        try:
            dt = datetime.strptime(data, "%d.%m.%Y").date()
        except ValueError:
            raise serializers.ValidationError("Дата должна быть в формате dd.mm.yyyy")

        if dt >= date_now:
            return dt
        raise serializers.ValidationError("Дата не может быть ранее текущей даты")


class DepositSerializer(serializers.ModelSerializer):
    date = DateFormatField()

    class Meta:
        model = Deposit
        exclude = ("created_at", "updated_at")
