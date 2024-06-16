from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

@csrf_exempt
def send_form(request):
    if request.method == 'POST':
        # request.POST.get(item_name='name in html)')
        phone = request.POST.get('phone')
        name = request.POST.get('name')
        
        email_message = f"""
        Номер телефона: {phone}
        Имя: {name}
        """
        try:
            email = request.POST.get('email')
            email_message = f"Email: {email}\n" + email_message
        except KeyError:
            pass
        
        try:
            service_type = request.POST.get('serviceType')
            email_message = f"Тип услуги: {service_type}\n" + email_message
        except KeyError:
            pass
        
        try:
            message = request.POST.get('message')
            email_message = email_message + f"\nСообщение: {email}"
        except KeyError:
            pass
    
        send_mail(
            'Заявка',
            email_message,
            'manager@site.ru',
            ['manager@site.ru'],
            fail_silently=False,
        )

        return JsonResponse({'message': 'Сообщение успешно отправлено'}, status=200)
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
