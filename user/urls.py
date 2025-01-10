from django.urls import path
from .views import UserListView, UserDetailView, UserCreateView

urlpatterns = [
    path("users/", UserListView.as_view(), name="user-list"),  # Admin only
    path("users/me/", UserDetailView.as_view(), name="user-detail"),  # Authenticated user
    path("users/register/", UserCreateView.as_view(), name="user-create"),  
]
