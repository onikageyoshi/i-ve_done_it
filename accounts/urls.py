from django.urls import path
from .views import LoanAccountList, LoanAccountDetail, LoanAccountCalculateBalance

urlpatterns = [
    path('loan-accounts/', LoanAccountList.as_view(), name='loanaccount-list'),
    path('loan-accounts/<int:pk>/', LoanAccountDetail.as_view(), name='loanaccount-detail'),
    path('loan-accounts/<int:pk>/calculate-balance/', LoanAccountCalculateBalance.as_view(), name='loanaccount-calculate-balance'),
]
