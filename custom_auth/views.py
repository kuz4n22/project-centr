from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.encoding import force_bytes, force_str
from django.utils.html import escape
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.decorators.csrf import csrf_exempt

from user.models import CustomUser


@csrf_exempt
def send_password_reset_form(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return JsonResponse({'error': 'Пользователь с таким email не найден'}, status=400)
       
        msg = EmailMessage(subject='Сброc пароля')
        
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        reset_url = request.build_absolute_uri(f'/password_reset/{uid}/{token}/')
        email_message = f'Для сброса пароля перейдите по ссылке: {reset_url}'
        email_message += f'\n\nЕсли вы не запрашивали создание нового пароля, просто проигнорируйте это письмо.'
        email_message += ' Ваш пароль не будет изменен.'
            
        try:
            msg.body = escape(email_message)
            msg.to = [email]
            msg.send(fail_silently=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
        return JsonResponse({'message': 'Письмо для сброса пароля отправлено на ваш email'}, status=200)
    return render(request, 'auth/password_reset_form.html')

def password_reset(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
        
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            new_password = request.POST.get('password')
            user.set_password(new_password)
            user.save()
            login(request, user)
            if user.is_staff:
                return JsonResponse({"redirect_url": "/manager/"}, status=200)
            else:
                return JsonResponse({"redirect_url": "/profile/"}, status=200)

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