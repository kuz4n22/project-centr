from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from custom_auth.decorators import manager_required
from user.forms import UserCreationForm
from user.models import Contract, CustomUser


@login_required
@manager_required
def manager_dashboard(request):
    clients = CustomUser.objects.filter(is_staff=False).prefetch_related("contracts")

    # Подготовка данных для упрощенного доступа на фронтенде
    active_clients = []
    completed_clients = []
    for client in clients:
        for contract in client.contracts.all():
            client = {
                "id": client.id,
                "first_name": client.first_name,
                "last_name": client.last_name,
                "phone_number": client.phone_number,
                "email": client.email,
                "password": client.password,
                "contract_id": contract.id,
                "service_type": contract.service_type,
                "contract_number": contract.contract_number,
                "contract_date": contract.contract_date,
                "status": contract.status,
                "is_done": contract.is_done,
                "is_last_phase": contract.is_last_phase,
                "max_phases": list(range(1, contract.max_phases()+1)),
            }

            if contract.is_done():
                client["completion_date"] = contract.completion_date
                completed_clients.append(client)
            else:
                active_clients.append(client)

    context = {
        "active_clients": active_clients,
        "completed_clients": completed_clients,
    }
    return render(request, "manager/dashboard.html", context)


@login_required
@manager_required
def add_client(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Пользователь успешно добавлен"})
        else:
            return JsonResponse(
                {"message": "Ошибка при добавлении пользователя", "error": form.errors},
                status=400,
            )
    form = UserCreationForm()
    return render(request, "manager/dashboard.html", {"form": form})


@login_required
@manager_required
def notify_next_phase(request, contract_id):
    # Добавить логику об отправке письма на почту
    return JsonResponse(
        {"message": "Уведомление о новом этапе успешно отправлено(Нет)"}, status=200
    )


@login_required
@manager_required
def next_phase(request, contract_id):
    contract = get_object_or_404(Contract, id=contract_id)
    if not contract.is_last_phase():
        contract.next_phase()
        return JsonResponse(
            {
                "message": "Новый этап успешно установлен",
                "new_status": contract.status,
            },
            status=200,
        )
    else:
        return JsonResponse(
            {"message": "Невозможно установить новый этап, так как этап уже последний",
            "error": "Невозможно установить новый этап, так как этап уже последний"}
        )


@login_required
@manager_required
def complete_project(request, contract_id):
    contract = get_object_or_404(Contract, id=contract_id)
    if contract.is_last_phase():
        contract.complete_project()
        return JsonResponse(
            {
                "message": "Проект успешно завершен",
                "completion_date": contract.completion_date,
            },
            status=200,
        )
    else:
        return JsonResponse(
            {
                "message": "Невозможно завершить проект, так как он не находится на последнем этапе",
                "error": "Невозможно завершить проект, так как он не находится на последнем этапе"
            },
            status=400,
        )


@login_required
@manager_required
def send_new_password(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    new_password = CustomUser.objects.make_random_password()
    # тут наеб пока)
    send_mail(
        "Ваш новый пароль",
        f"Ваш новый пароль: {new_password}",
        "mail@mail.com",
        [user.email],
        fail_silently=False,
    )
    user.set_password(new_password)
    user.save()
    return JsonResponse(
        {"message": "Новый пароль успешно отправлен на вашу почту"}, status=200
    )
