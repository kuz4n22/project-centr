from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'contracts', views.ContractViewSet)

urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('', views.main_page, name='main'),
    path('apartments/', views.apartments_page, name='apartments'),
    path('spaces/', views.spaces_page, name='spaces'),
    path('buildings/', views.buildings_page, name='buildings'),
    path('cadastr/', views.cadastr_page, name='cadastr'),
]
