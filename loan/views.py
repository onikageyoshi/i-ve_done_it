from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Loan
from .serializers import LoanSerializer, BorrowerSerializer
from rest_framework import response, status, permissions, views
from drf_yasg.utils import swagger_auto_schema



class LoanListView(views.APIView):
    def get(self, request):
        loans = Loan.objects.all()
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)
   
    @swagger_auto_schema(request_body=LoanSerializer)
    def post(self, request):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            permission_classes = [permissions.Allowany]
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoanDetailView(views.APIView):
    def get(self, request, pk):
        try:
            loan = Loan.objects.get(pk=pk)
        except Loan.DoesNotExist:
            return Response({"error": "Loan not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = LoanSerializer(loan)
        permission_classes = [permissions.Allowany]
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=LoanSerializer)
    def post(self, request):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the loan with provided data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

