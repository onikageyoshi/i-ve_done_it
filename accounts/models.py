from .choices import  CURRENCY_CHOICES
import uuid
from django.db import models
from django.utils.timezone import now

class LoanAccount(models.Model):
    ACCOUNT_STATUS_CHOICES = [
        ('active', 'Active'),
        ('closed', 'Closed'),
        ('defaulted', 'Defaulted'),
        ('pending', 'Pending Approval'),
    ]

    LOAN_TYPE_CHOICES = [
        ('personal', 'Personal Loan'),
        ('business', 'Business Loan'),
        ('education', 'Education Loan'),
    ]

    loan_account_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    account_number = models.CharField(max_length=20, unique=True)
    borrower_name = models.CharField(max_length=100)
    borrower_email = models.EmailField()
    loan_type = models.CharField(max_length=20, choices=LOAN_TYPE_CHOICES)
    principal_amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2) 
    loan_term_months = models.IntegerField()  
    start_date = models.DateField(default=now)
    end_date = models.DateField(null=True, blank=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=ACCOUNT_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"LoanAccount({self.account_number}, {self.borrower_name})"

    def calculate_monthly_payment(self):
        """
        Calculate the fixed monthly payment using the amortization formula.
        """
        if self.interest_rate == 0:
            return self.principal_amount / self.loan_term_months
        
        monthly_rate = (self.interest_rate / 100) / 12
        numerator = self.principal_amount * monthly_rate * (1 + monthly_rate) ** self.loan_term_months
        denominator = (1 + monthly_rate) ** self.loan_term_months - 1
        return round(numerator / denominator, 2)

    def is_overdue(self):
        """
        Check if the loan is overdue based on the end date.
        """
        if self.end_date and now().date() > self.end_date:
            return True
        return False
