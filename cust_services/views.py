from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import CustomerServiceRequest
from .serializers import CustomerServiceRequestSerializer

class CustomerServiceRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        List all customer service requests for the logged-in user.
        """
        requests = CustomerServiceRequest.objects.filter(customer=request.user)
        serializer = CustomerServiceRequestSerializer(requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new customer service request.
        """
        data = request.data.copy()
        data['customer'] = request.user.id  # Attach the logged-in user to the request.
        serializer = CustomerServiceRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateCustomerServiceRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        """
        Update the status of an existing customer service request.
        """
        try:
            service_request = CustomerServiceRequest.objects.get(pk=pk, customer=request.user)
        except CustomerServiceRequest.DoesNotExist:
            return Response({"error": "Service request not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerServiceRequestSerializer(service_request, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

