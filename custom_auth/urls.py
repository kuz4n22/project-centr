from django.urls import path
from .views import login_view, logout_view
from custom_auth.views import CustomPasswordResetView, CustomPasswordResetConfirmView


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]