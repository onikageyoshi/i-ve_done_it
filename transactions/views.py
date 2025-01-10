from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Loan_withdrawal, Loan_transfer
from .serializers import Loan_withdrawalSerializer, Loan_transferSerializer
from rest_framework import response, status, permissions, views
from drf_yasg.utils import swagger_auto_schema


class LoanWithdrawalListCreateView(views.APIView):
    """
    Handles listing all loan withdrawals and creating a new loan withdrawal.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        withdrawals = Loan_withdrawal.objects.filter(user=request.user)
        serializer = Loan_withdrawalSerializer(withdrawals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = Loan_withdrawalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoanWithdrawalDetailView(views.APIView):
    """
    Handles retrieving details of a specific loan withdrawal.
    """
    permission_classes = [permissions.AllowAny]


    
    def get(self, request, pk):
        try:
            withdrawal = Loan_withdrawal.objects.get(id=pk, user=request.user)
        except Loan_withdrawal.DoesNotExist:
            return Response({"error": "Loan withdrawal not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = Loan_withdrawalSerializer(withdrawal)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=Loan_withdrawalSerializer)
    def post(self, request):
        serializer = Loan_withdrawalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Save the instance with the current user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  



class LoanTransferListCreateView(views.APIView):
    """
    Handles listing all loan transfers and creating a new loan transfer.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transfers = Loan_transfer.objects.filter(user=request.user)
        serializer = Loan_transferSerializer(transfers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=Loan_transferSerializer)
    def post(self, request):
        serializer = Loan_transferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoanTransferDetailView(views.APIView):
    """
    Handles retrieving details of a specific loan transfer.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            transfer = Loan_transfer.objects.get(id=pk, user=request.user)
        except Loan_transfer.DoesNotExist:
            return Response({"error": "Loan transfer not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = Loan_transferSerializer(transfer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=Loan_transferSerializer)
    def post(self, request):
        serializer = Loan_transferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Associate the loan transfer with the current user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 