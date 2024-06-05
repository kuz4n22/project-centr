from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Contract
from .forms import UserCreationForm, CustomUserChangeForm

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('phone_number', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'phone_number',  'password', 'email', 'service_type', 'contract_number', 'contract_date', 'is_staff', 'is_active', 'is_superuser'),
        }),
    )
    search_fields = ('phone_number', 'email', 'first_name', 'last_name')
    ordering = ('phone_number',)
    filter_horizontal = ('groups', 'user_permissions',)
    
admin.site.register(Contract)
