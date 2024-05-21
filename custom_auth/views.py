from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy


#Вход/выход
def login_view(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, username=phone, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('manager_dashboard')
            else:
                return redirect('user_profile')
        else:
            return render(request, 'auth/login.html', {'error': 'Неверные данные'})
    return render(request, 'auth/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


#Сброс пароля
class CustomPasswordResetView(PasswordResetView):
    template_name = 'auth/password_reset.html'
    email_template_name = 'auth/password_reset_email.html' # шаблон того как выглядит письмо сброса пароля
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'auth/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')