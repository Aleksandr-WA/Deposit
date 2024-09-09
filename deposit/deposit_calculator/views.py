from dateutil.relativedelta import relativedelta
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DepositSerializer


class DepositCalculator(APIView):
    def post(self, request):
        serializer = DepositSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["calculated_value"] = self.calculate_deposit(
            serializer
        )
        serializer.save()
        return Response(
            serializer.validated_data["calculated_value"],
            status=status.HTTP_200_OK,
        )

    @staticmethod
    def calculate_deposit(serializer):
        future_value = {}
        date = serializer.validated_data["date"]
        periods = serializer.validated_data["periods"]
        amount = serializer.validated_data["amount"]
        rate = serializer.validated_data["rate"]
        monthly_rate = rate / 12 / 100
        for month in range(1, periods + 1):
            key_date = (date + relativedelta(months=month)).strftime("%d.%m.%Y")
            future_value[key_date] = round(amount * (1 + monthly_rate) ** month, 2)
        return future_value
