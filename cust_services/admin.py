from django.contrib import admin
from .models import CustomerServiceRequest

@admin.register(CustomerServiceRequest)
class Cust_servicesAdmin(admin.ModelAdmin):
    list_display = ['customer', 'subject', 'description']
    list_filter = list_display + ['customer', 'subject', 'description']
    search_fields = list_display

