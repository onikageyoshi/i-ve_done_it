from django.contrib import admin
from customer.models import Customer

@admin.register(Customer)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']
    list_filter = list_display + ['id']
    search_fields = list_display

