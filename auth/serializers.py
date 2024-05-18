from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email', 'phone', 'password', 'first_name', 'last_name']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             email=validated_data['email'],
#             phone=validated_data['phone'],
#             password=validated_data['password'],
#             first_name=validated_data.get('first_name', ''),
#             last_name=validated_data.get('last_name', '')
#         )
#         return user

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, data):
        phone_number = data.get('phone_number')
        password = data.get('password')

        if phone_number and password:
            user = authenticate(request=self.context.get('request'), phone_number=phone_number, password=password)

            if not user:
                raise serializers.ValidationError('Неверный логин или пароль')
            
            refresh = RefreshToken.for_user(user)
            return {
                'phone_number': user.phone_number,
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
        else:
            raise serializers.ValidationError('Должен быть введен номер телефона или пароль')
