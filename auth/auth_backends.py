from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from user.models import CustomUser
from django.contrib.auth import authenticate


User = get_user_model()

class PhoneBackend(BaseBackend): 
    def authenticate(self, request, phone_number=None, password=None):
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
