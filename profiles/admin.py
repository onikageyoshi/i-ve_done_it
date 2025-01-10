from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'state']
    list_filter = list_display + ['user']
    search_fields = list_display

