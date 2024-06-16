from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('custom_auth.urls')),
    path('', include('user.urls')),
    path('manager/', include('manager.urls')),
    path('__reload__/', include('django_browser_reload.urls')),
]

handler404 = 'user.views.custom_404'
