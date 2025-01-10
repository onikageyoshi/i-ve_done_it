from django.contrib import admin
from . models import User

@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']
    list_filter = list_display + ['first_name', 'email']
    search_fields = list_display

