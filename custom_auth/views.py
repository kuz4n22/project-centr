from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.http import JsonResponse


# Вход/выход
def login_view(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        if not phone or not password:
            return JsonResponse({"error": "Необходимо указать телефон и пароль"}, status=400)

        user = authenticate(request, username=phone, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect("manager_dashboard")
            else:
                return redirect("user_profile")
        else:
            return JsonResponse({"error": "Неверные данные"}, status=400)
    return render(request, "auth/login.html")





# Сброс пароля
# Разобраться что это
class CustomPasswordResetView(PasswordResetView):
    template_name = "auth/password_reset.html"
    # шаблон того как выглядит письмо сброса пароля
    email_template_name = "auth/password_reset_email.html"
    success_url = reverse_lazy("password_reset_done")


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "auth/password_reset_confirm.html"
    success_url = reverse_lazy("password_reset_complete")
