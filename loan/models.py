from django.db import models
from django.contrib.auth import get_user_model 


class Borrower(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.phone_number

class Loan(models.Model):
    LOAN_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('PAID_OFF', 'Paid Off'),
    ]
    
    LOAN_TYPES = [
        ("PERSONAL","PERSONAL"),
        ("EDUCATIONAL","EDUCATIONAL"),
        ("BUSINESS","BUSINESS"),
    ] 

    
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name='loans')
    amount = models.DecimalField(max_digits=12, decimal_places=2)  
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)  
    term_months = models.PositiveIntegerField()  
    start_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=LOAN_STATUS_CHOICES, default='PENDING')
    loan_types = models.CharField(max_length=20, choices=LOAN_TYPES, default="PERSONAL" )
    
    def __str__(self):
        return f"Loan of {self.amount} to {self.borrower}"

    @property
    def total_repayment_amount(self):
        """Calculates the total amount to be paid back including interest"""
        return self.amount * (1 + self.interest_rate / 100)
    
    def get_repayment_schedule(self):
        """Returns a repayment schedule (for simplicity, assuming equal installments)"""
        monthly_repayment = self.total_repayment_amount / self.term_months
        return monthly_repayment
    
    def calculate_monthly_payment(self):
        """Calculate the monthly payment using the formula for an amortizing loan."""
        monthly_rate = self.interest_rate / 100 / 12
        denominator = (1 - (1 + monthly_rate) ** -self.loan_term)
        if denominator == 0:
            return self.loan_amount / self.loan_term
        return self.loan_amount * monthly_rate / denominator

    def make_payment(self, amount, date):
        """Record a payment towards the loan."""
        self.payments.append({"amount": amount, "date": date})
        self.loan_amount -= amount
        if self.loan_amount <= 0:
            self.status = "Paid"

    def remaining_balance(self):
        """Calculate the remaining balance of the loan."""
        return max(self.loan_amount, 0)



class Repayment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='repayments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Payment amount
    date = models.DateField()
    status = models.CharField(max_length=20, choices=[('on_time', 'On Time'), ('defaulted', 'Defaulted')])

    def __str__(self):
        return f"Repayment {self.id} - Loan {self.loan.id}"