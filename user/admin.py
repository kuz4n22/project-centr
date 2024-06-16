import re

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, UserCreationForm
from .models import Contract, CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('phone_number', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'contracts')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'phone_number',  'password', 'email', 'service_type', 'contract_number', 'contract_date', 'address', 'is_staff', 'is_active', 'is_superuser'),
        }),
    )
    search_fields = ('phone_number', 'email', 'first_name', 'last_name')
    ordering = ('phone_number',)
    filter_horizontal = ('groups', 'user_permissions',)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            user = form.save(commit=False)
            full_name = form.cleaned_data["full_name"]

            name_parts = re.split(r"\s+", full_name.strip())
            user.first_name, user.last_name = name_parts[0], " ".join(name_parts[1:])
            user.set_password(form.cleaned_data["password"])

            user.save()
            Contract.objects.create(
                user=user,
                contract_number=form.cleaned_data["contract_number"],
                service_type=form.cleaned_data["service_type"],
                contract_date=form.cleaned_data["contract_date"],
                address=form.cleaned_data["address"],
            )
        else:
            super().save_model(request, obj, form, change)
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Contract)
