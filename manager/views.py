from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from custom_auth.decorators import manager_required
from user.models import Contract, CustomUser
from .forms import UserCreationForm


@login_required
@manager_required
def manager_dashboard(request):
    clients = CustomUser.objects.filter(
        is_staff=False).order_by("-contract_date")
    context = {
        "clients": clients,
    }
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
    return render(request, 'manager/dashboard.html', {'form': form})

@login_required
@manager_required
def notify_next_phase(request, contract_id):
    contract = get_object_or_404(Contract, id=contract_id)
    contract.next_phase()
    return redirect("manager_dashboard")


@login_required
@manager_required
def complete_project(request, contract_id):
    contract = get_object_or_404(Contract, id=contract_id)
    # проверка на последний этап
    if contract.is_last_phase():
        contract.complete_project()
    return redirect("manager_dashboard")


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
    return redirect("manager_dashboard")
