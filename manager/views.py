from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from custom_auth.decorators import manager_required

@login_required
@manager_required
def manager_dashboard(request):
    manager = request.user
    context = {
        "manager": manager
    }
    return render(request, 'manager/dashboard.html', context)
