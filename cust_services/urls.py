from django.urls import path
from .views import CustomerServiceRequestView, UpdateCustomerServiceRequestView

urlpatterns = [
    path('service-requests/', CustomerServiceRequestView.as_view(), name='service-request-list-create'),
    path('service-requests/<int:pk>/', UpdateCustomerServiceRequestView.as_view(), name='service-request-update'),
]
