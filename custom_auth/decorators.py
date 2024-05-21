
from django.http import HttpResponseForbidden

def manager_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("Вы не авторизованы для доступа к этой странице.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func
