from datetime import datetime
import pytest
from dateutil.relativedelta import relativedelta
from rest_framework import status
from rest_framework.test import APIClient
from deposit_calculator.views import DepositCalculator


@pytest.mark.django_db
def test_calculate_deposit_success():
    client = APIClient()
    request_data = {"date": "30.08.2024", "amount": 10000, "rate": 5, "periods": 12}
    response = client.post("/api/deposit/calculator/", request_data, format="json")
    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()
    assert isinstance(response_data, dict)
    assert len(response_data) == 12
    for key in response_data:
        assert isinstance(key, str)
        assert isinstance(response_data[key], float)


@pytest.mark.django_db
def test_calculate_deposit_invalid_data():
    client = APIClient()
    request_data = {
        "date": "01.08.2023",
        "amount": "invalid-amount",
        "rate": "invalid-rate",
        "periods": "invalid-periods",
    }
    response = client.post("/api/deposit/calculator/", request_data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "date" in response.json()
    assert "amount" in response.json()
    assert "rate" in response.json()
    assert "periods" in response.json()


@pytest.mark.django_db
def test_calculate_deposit_missing_field():
    client = APIClient()
    request_data = {
        "date": "2024-08-01",
        "amount": 1000,
        "rate": 5,
        # Периоды отсутствуют
    }
    response = client.post("/api/deposit/calculator/", request_data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "periods" in response.json()


def test_calculate_deposit():
    date = datetime(2024, 8, 30)
    amount = 10000
    rate = 5.0
    periods = 6
    expected_value = {
        (date + relativedelta(months=i)).strftime("%d.%m.%Y"): round(
            amount * (1 + rate / 12 / 100) ** i, 2
        )
        for i in range(1, periods + 1)
    }
    calculated_value = DepositCalculator.calculate_deposit(date, amount, rate, periods)
    assert calculated_value == expected_value
