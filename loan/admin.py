from django.contrib import admin
from loan.models import Loan, Borrower


@admin.register(Loan)
class LoansAdmin(admin.ModelAdmin):
    list_display = ['status', 'borrower', 'amount']
    list_filter = list_display + ['status']
    search_fields = list_display

@admin.register(Borrower)
class BorrowersAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone_number']
    list_filter = list_display + ['phone_number']
    search_fields = list_display


