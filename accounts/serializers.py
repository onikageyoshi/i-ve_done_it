from rest_framework import serializers
from rest_framework import serializers
from .models import LoanAccount

class LoanAccountSerializer(serializers.ModelSerializer):
    monthly_payment = serializers.SerializerMethodField()
    overdue = serializers.SerializerMethodField()

    class Meta:
        model = LoanAccount
        fields = [
            'account_number', 'borrower_name', 'borrower_email', 
            'loan_type', 'principal_amount', 'interest_rate', 
            'loan_term_months', 'start_date', 'end_date', 
            'balance', 'status', 'created_at', 'updated_at', 
            'monthly_payment', 'overdue'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'monthly_payment', 'overdue']

    def get_monthly_payment(self, obj):
        return obj.calculate_monthly_payment()

    def get_overdue(self, obj):
        return obj.is_overdue()
