from django.urls import path
from . import views

urlpatterns = [
    path("loan/", views.LoanListView.as_view()),
]