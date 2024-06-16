from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),

    path('password_reset/', views.send_password_reset_form, name='password_reset_form'),
    path('password_reset/<uidb64>/<token>/', views.password_reset, name='password_reset'),
]