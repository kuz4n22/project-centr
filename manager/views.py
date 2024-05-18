# from rest_framework import generics
from rest_framework import viewsets
from user.models import CustomUser
from user.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

# class RegisterView(generics.CreateAPIView):
#     serializer_class = RegisterSerializer
#     permission_classes = [AllowAny]
    
class ManagerUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(is_staff=False)
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
