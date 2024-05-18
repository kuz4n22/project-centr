from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, login_page



urlpatterns = [
    path ('auth/', login_page, name = 'auth'),
    path('api/token/', LoginView.as_view(), name='login'),
]
