# from rest_framework import serializers
# from user.models import CustomUser

# class ManagerUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['contract_number', 'first_name', 'last_name', 'phone_number', 'email', 'password', 'service_type', 'contract_date', 'status']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = CustomUser.objects.create(
#             contract_number=validated_data['contract_number'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#             phone_number=validated_data['phone_number'],
#             email=validated_data['email'],
#             service_type=validated_data['service_type'],
#             contract_date=validated_data['contract_date'],
#             status=validated_data['status'],
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
