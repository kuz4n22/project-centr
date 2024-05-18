from rest_framework import serializers
from .models import CustomUser, Contract

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['contract_number', 'service_type', 'contract_date', 'completion_date', 'status']

class UserSerializer(serializers.ModelSerializer):
    contracts = ContractSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'first_name', 'last_name', 'email', 'contracts']
