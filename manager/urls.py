from django.urls import path

from . import views

urlpatterns = [
    path('', views.manager_dashboard, name='manager_dashboard'),
    path('add_client/', views.add_client, name='add_client'),
    path('next_phase/<int:contract_id>/', views.next_phase, name='next_phase'),
    path('notify_next_phase/<int:contract_id>/', views.notify_next_phase, name='notify_next_phase'),
    path('complete_project/<int:contract_id>/', views.complete_project, name='complete_project'),
    path('send_new_password/<int:user_id>/', views.send_new_password, name='send_new_password'),
]
