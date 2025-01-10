from rest_framework import serializers
from .models import Borrower, Loan

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ['id', 'user', 'phone_number', 'address']

class LoanSerializer(serializers.ModelSerializer):
    borrower = BorrowerSerializer(read_only=True)  # Include borrower details in the response
    
    class Meta:
        model = Loan
        fields = [
            'id', 'borrower', 'amount', 'interest_rate', 'term_months', 'start_date', 
            'due_date', 'status', 'loan_types', 'total_repayment_amount', 'get_repayment_schedule'
        ]
