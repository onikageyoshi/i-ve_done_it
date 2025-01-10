from django.contrib import admin
from .models import  Loan_withdrawal, Loan_transfer


@admin.register(Loan_withdrawal)
class Loan_withdrawalsAdmin(admin.ModelAdmin):
    list_display = ['account_number', 'transaction_type']
    list_filter = list_display + ['account_number']
    search_fields = list_display

@admin.register(Loan_transfer)
class Loan_transfersAdmin(admin.ModelAdmin):
    list_display = ['source_account_number', 'destination_account_number']
    list_filter = list_display + ['source_account_number']
    search_fields = list_display

