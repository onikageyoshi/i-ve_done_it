from django.urls import path
from .views import (
    LoanWithdrawalListCreateView,
    LoanWithdrawalDetailView,
    LoanTransferListCreateView,
    LoanTransferDetailView,
)

urlpatterns = [
    path('loan-withdrawals/', LoanWithdrawalListCreateView.as_view(), name='loan-withdrawal-list-create'),
    path('loan-withdrawals/<uuid:pk>/', LoanWithdrawalDetailView.as_view(), name='loan-withdrawal-detail'),
    path('loan-transfers/', LoanTransferListCreateView.as_view(), name='loan-transfer-list-create'),
    path('loan-transfers/<uuid:pk>/', LoanTransferDetailView.as_view(), name='loan-transfer-detail'),
]
