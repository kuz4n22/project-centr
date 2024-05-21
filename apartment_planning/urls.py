from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('manager/', include('manager.urls')),
    path('', include('custom_auth.urls')),
    path('__reload__/', include('django_browser_reload.urls')),
]
