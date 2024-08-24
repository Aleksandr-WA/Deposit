from django.urls import path
from .views import DepositCalculator

urlpatterns = [
    path('calculator/', DepositCalculator.as_view()),
]