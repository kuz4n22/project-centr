from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def send_password_reset_form(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            reset_url = request.build_absolute_uri(f'/reset_password/{uid}/{token}/')

            send_mail(
                'Сброс пароля',
                f'Для сброса пароля перейдите по ссылке: {reset_url}',
                'password_reset@site.ru',
                [email],
                fail_silently=False,
            )

            return JsonResponse({'message': 'Письмо для сброса пароля отправлено на ваш email'}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Пользователь с таким email не найден'}, status=400)
    return render(request, 'auth/password_reset_form.html')

def password_reset(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            new_password = request.POST.get('password')
            user.set_password(new_password)
            user.save()
            return redirect('login')

        return render(request, 'auth/password_reset.html', {'uidb64': uidb64, 'token': token})
    else:
        return render(request, 'auth/password_reset.html', {'error': 'Недействительная ссылка для сброса пароля'})

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
                return JsonResponse({"redirect_url": "/manager/"}, status=200)
            else:
                return JsonResponse({"redirect_url": "/profile/"}, status=200)
        else:
            return JsonResponse({"error": "Неверные данные"}, status=400)
    return render(request, "auth/login.html")