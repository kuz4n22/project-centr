from rest_framework import viewsets
from user.models import CustomUser
from user.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class ManagerUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(user_type='client')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_type='client')
