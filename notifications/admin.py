from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ['user', 'timestamp', 'amount']
    list_filter = list_display + ['user']
    search_fields = list_display

