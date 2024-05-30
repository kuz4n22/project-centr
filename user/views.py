from rest_framework import viewsets
from .models import CustomUser, Contract
from .serializers import UserSerializer, ContractSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.filter(is_staff=False)
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]


# class ContractViewSet(viewsets.ModelViewSet):
#     queryset = Contract.objects.all()
#     serializer_class = ContractSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

def main_page(request):
    return render(request, 'pages/main.html')

## вывод: на двух стульях не усидеть
@login_required
def user_profile(request):
    # user = request.user
    # context = {
    #     "user": user
    # }
    return render(request, "user/profile.html")
