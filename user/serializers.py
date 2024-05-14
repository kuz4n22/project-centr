from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'contract_number', 'first_name', 'last_name', 'phone_number', 'email', 'service_type', 'contract_date', 'completion_date', 'status']
