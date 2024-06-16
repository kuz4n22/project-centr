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
    path('form/', views.form_page, name='form'),
    path('form-sent/', views.form_sent_page, name='form_sent'),
    path('calculator/', views.calculator_page, name='calculator'),
    path('politic/', views.politic_page, name='politic'),
    path('contacts/', views.contacts_page, name='contacts'),
    path('about/', views.about_page, name='about'),

    path('send_form/', views.send_form, name='send_contact_form'),

    # delete before prod
    path('error/', views.error_page, name='error'),
    # 
]
