from django.contrib import admin

from accounts.models import LoanAccount

@admin.register(LoanAccount)
class AccountsAdmin(admin.ModelAdmin):
    list_display = ['loan_type', 'borrower_name', 'status']
    search_fields = list_display

    
