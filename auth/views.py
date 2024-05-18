from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from user.serializers import UserSerializer
from django.shortcuts import render

def login_page(request):
    return render(request, 'auth/auth.html')

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
