from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def send_form(request):
    if request.method == 'POST':
        subject='Новая заявка'
        msg = EmailMessage(subject=subject)
        
        phone = request.POST.get('phone')
        name = request.POST.get('name')
        email_message = f'Получена новая заявка.'
        email_message += f'\nИмя: {name}\nНомер телефона: {phone}'

        email = request.POST.get('email')
        if email:
            email_message += f"\nEmail: {email}"

        service_type = request.POST.get('serviceType')
        if service_type:
            email_message += f"\nТип услуги: {service_type}"

        message = request.POST.get('message')
        if message:
            email_message += f"\nСообщение: {message}"

        try:
            msg.body = escape(email_message)
            msg.to = [manager[-1] for manager in settings.MANAGERS]
            msg.send(fail_silently=False)
            return JsonResponse({'message': 'Сообщение успешно отправлено'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Неверный метод запроса'}, status=400)

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
    return render(request, "user/profile.html")
