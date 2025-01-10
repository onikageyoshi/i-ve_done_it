from rest_framework import serializers

from .models import  Loan_transfer, Loan_withdrawal


class Loan_withdrawalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan_withdrawal
        fields = '__all__'


class CreateLoan_WithdrawalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan_withdrawal
        fields = ('account_number','amount')                 


class Loan_transferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_transfer
        fields = "__all__"



class CreateLoan_transferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_transfer
        fields = ['amount', 'destination_account_number']

