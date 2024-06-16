from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),

    path('send_reset_password_email/', views.send_reset_password_email, name='send_reset_password_email'),
    path('reset_password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
]