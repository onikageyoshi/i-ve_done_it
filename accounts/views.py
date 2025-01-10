from rest_framework.views import APIView
from rest_framework import permissions, response, status, views
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import LoanAccount
from .serializers import LoanAccountSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema


from rest_framework.response import Response
from rest_framework import status
from .serializers import LoanAccountSerializer

class LoanAccountDetail(views.APIView):
    def get(self, request, pk):
        # Fetch the loan account and serialize it
        loan_account = LoanAccount.objects.get(pk=pk)
        serializer = LoanAccountSerializer(loan_account)
        
        # Return a successful response with the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)




class LoanAccountList(views.APIView):
    """
    Handles listing all loan accounts and creating a new loan account.
    """
    permission_classes = [AllowAny]  # Allows anyone to access this view

    def get(self, request):
        loan_accounts = LoanAccount.objects.all()
        serializer = LoanAccountSerializer(loan_accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LoanAccountDetail(views.APIView):
    def post(self, request):
        serializer = LoanAccountSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=400)













































        


class LoanAccountDetail(views.APIView):
    """
    Handles retrieving, updating, and deleting a specific loan account by its ID.
    """
    permission_classes = [AllowAny]  # Allows anyone to access this view

    def get_object(self, pk):
        return get_object_or_404(LoanAccount, pk=pk)

    def get(self, request, pk):
        loan_account = self.get_object(pk)
        serializer = LoanAccountSerializer(loan_account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        loan_account = self.get_object(pk)
        serializer = LoanAccountSerializer(loan_account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        loan_account = self.get_object(pk)
        loan_account.delete()
        return Response({"message": "Loan account deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class LoanAccountCalculateBalance(views.APIView):
    """
    Custom endpoint for calculating and retrieving the balance of a specific loan account.
    """
    permission_classes = [AllowAny]  # Allows anyone to access this view

    def get(self, request, pk):
        loan_account = get_object_or_404(LoanAccount, pk=pk)
        return Response({
            'account_number': loan_account.account_number,
            'balance': loan_account.balance,
        }, status=status.HTTP_200_OK)
