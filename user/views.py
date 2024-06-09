from rest_framework import viewsets
from .models import CustomUser, Contract
from .serializers import UserSerializer, ContractSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def main_page(request):
    return render(request, 'pages/main.html')

def apartments_page(request):
    return render(request, 'pages/offers/apartments.html')

def spaces_page(request):
    return render(request, 'pages/offers/spaces.html')

def buildings_page(request):
    return render(request, 'pages/offers/buildings.html')

def cadastr_page(request):
    return render(request, 'pages/offers/cadastr.html')

def form_page(request):
    return render(request, 'user/form.html')

def form_sent_page(request):
    return render(request, 'user/form_sent.html')

def calculator_page(request):
    return render(request, 'user/calculator.html')

def politic_page(request):
    return render(request, 'pages/politic.html')

def contacts_page(request):
    return render(request, 'pages/contacts.html')

def about_page(request):
    return render(request, 'pages/about.html')

# delete before prod
def error_page(request):
    return render(request, 'pages/404.html')

def custom_404(request, exception):
    return render(request, 'pages/404.html', status=404)


## вывод: на двух стульях не усидеть
@login_required
def user_profile(request):
    # user = request.user
    # context = {
    #     "user": user
    # }
    return render(request, "user/profile.html")
