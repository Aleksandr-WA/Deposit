from datetime import datetime, date
from rest_framework import serializers
from .models import Deposit


class DateFormatField(serializers.Field):
    def to_representation(self, value):
        if value:
            return value.strftime('%d.%m.%Y')
        return ''

    def to_internal_value(self, data):
        if data:
            try:
                dt = datetime.strptime(data, '%d.%m.%Y')
                if dt > datetime.today():
                    return dt
                else:
                    raise serializers.ValidationError('Дата не может быть ранее текущей даты')
            except ValueError:
                raise serializers.ValidationError('Дата должна быть в формате dd.mm.yyyy')
        return None


class DepositSerializer(serializers.ModelSerializer):
    date = DateFormatField()

    class Meta:
        model = Deposit
        fields = '__all__'
