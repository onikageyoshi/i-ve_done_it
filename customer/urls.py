from django.urls import path
from . import views

urlpatterns = [
    path("customer/", views.CustomerView.as_view()),
]