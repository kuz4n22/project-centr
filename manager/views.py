from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from custom_auth.decorators import manager_required
from user.forms import UserCreationForm
from user.models import Contract, CustomUser


@login_required
@manager_required
def manager_dashboard(request):
    active_clients = CustomUser.objects.filter(is_staff=False, contracts__status__gt=0).order_by("-contracts__contract_date").distinct()
    completed_clients = CustomUser.objects.filter(is_staff=False, contracts__status=0).order_by("-contracts__contract_date").distinct()

    # # Отладочная информация
    # print("Active clients:", active_clients)
    # print("Completed clients:", completed_clients)

    context = {"active_clients": active_clients, "completed_clients": completed_clients}
    return render(request, "manager/dashboard.html", context)


@login_required
@manager_required
def add_client(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно добавлен')
            return redirect('manager_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'manager/add_client.html', {'form': form})

@login_required
@manager_required
def notify_next_phase(request, contract_id):
    contract = get_object_or_404(Contract, id=contract_id)
    contract.next_phase()
    # Добавить логику об отправке письма на почту 
    return JsonResponse({'message': 'Уведомление о новом этапе успешно отправлено'}, status=200)

@login_required
@manager_required
def complete_project(request, contract_id):
    contract = get_object_or_404(Contract, id=contract_id)
    if contract.is_last_phase():
        contract.complete_project()
        return JsonResponse({'message': 'Проект успешно завершен'}, status=200)
    else:
        return JsonResponse({'error': 'Невозможно завершить проект, так как он не находится на последнем этапе'}, status=400)

@login_required
@manager_required
def send_new_password(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    new_password = CustomUser.objects.make_random_password()
    user.set_password(new_password)
    user.save()
    send_mail(
        "Ваш новый пароль",
        f"Ваш новый пароль: {new_password}",
        "mail@mail.com",
        [user.email],
        fail_silently=False,
    )
    #тут наеб пока)
    return JsonResponse({'message': 'Новый пароль успешно отправлен на вашу почту'}, status=200)
