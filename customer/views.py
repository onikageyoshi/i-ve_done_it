from django.shortcuts import render
from rest_framework import response, status, permissions, views
from drf_yasg.utils import swagger_auto_schema
from .models import Customer
from .serializers import Create_customerSerializer, CustomerSerializer
from rest_framework import response, status, permissions, views
from drf_yasg.utils import swagger_auto_schema

class CustomerView(views.APIView):
    """
    Handles Customer operations.
    """
    
    @swagger_auto_schema(request_body=CustomerSerializer)
    def post(self, request):
        """
        Create a new customer using the CustomerSerializer.
        """
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateCustomerView(views.APIView):
    """
    Handles creation of new customers using Create_customerSerializer.
    """
    
    @swagger_auto_schema(request_body=CustomerSerializer)
    def post(self, request):
        """
        Create a new customer using the Create_customerSerializer.
        """
        serializer = Create_customerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KYCView(views.APIView):
    """
    Handles KYC submission.
    """
    
    
    def post(self, request):
        """
        Submit KYC information using the KYCSerializer.
        """
        serializer = KYCSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)