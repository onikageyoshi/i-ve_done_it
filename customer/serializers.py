from rest_framework import serializers

from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class Create_customerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'                

class KYCSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ['verified', 'submitted_at', 'updated_at']
