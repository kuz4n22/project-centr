from django.contrib import admin
from .models import CustomUser, Contract
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


class ContractInline(admin.TabularInline):
    model = Contract
    extra = 1
    
class CustomUserAdmin(BaseUserAdmin):
    inlines = [ContractInline]
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('phone_number', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('phone_number', 'first_name', 'last_name', 'email')
    ordering = ('phone_number',)

admin.site.register(CustomUser, CustomUserAdmin)