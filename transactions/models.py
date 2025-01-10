import uuid

from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

TRANSACTION_STATUS_CHOICES = (
    ("SUCCESSFUL", "SUCCESSFUL"),
    ("FAILED", "FAILED"),
    ("PENDING", "PENDING"),
)

TRANSACTION_CHOICES = (
    ("WITHDRAWAL","WITHDRAWAL"),
    ("REPAYMENT","REPAYMENT"),
)

class Transaction(models.Model):    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=15, choices=TRANSACTION_STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-timestamp']

class Loan_withdrawal(Transaction):
    account_number = models.CharField(max_length=11)
    transaction_type = models.CharField(max_length=30, choices=TRANSACTION_CHOICES)
    

class Loan_transfer(Transaction):
    source_account_number = models.CharField(max_length=11)
    destination_account_number = models.CharField(max_length=11)




