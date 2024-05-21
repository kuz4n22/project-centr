from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/', include('user.urls')),
    path('user/', include('user.urls')),
    path('manager/', include('manager.urls')),
    path('__reload__/', include('django_browser_reload.urls')),
]
