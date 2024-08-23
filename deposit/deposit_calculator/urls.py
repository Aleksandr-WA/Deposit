from django.urls import path
from deposit_calculator.views import DepositCalculator

urlpatterns = [
    path('calculator/', DepositCalculator.as_view()),
]