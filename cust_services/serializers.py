from rest_framework import serializers
from .models import CustomerServiceRequest

class CustomerServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerServiceRequest
        fields = ['id', 'customer', 'subject', 'description', 'status', 'created_at', 'updated_at']
        read_only_fields = ['customer', 'created_at', 'updated_at']


