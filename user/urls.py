from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'contracts', views.ContractViewSet)

urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('', include(router.urls)),

]
