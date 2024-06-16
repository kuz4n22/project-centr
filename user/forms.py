import re
from django.utils import timezone
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Contract


class UserCreationForm(forms.ModelForm):
    full_name = forms.CharField(label="Имя Фамилия", max_length=60)
    service_type = forms.ChoiceField(
        label="Тип услуги", choices=Contract.ServiceTypeChoices.choices
    )
    phone_number = forms.CharField(label="Номер телефона", max_length=15)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    email = forms.EmailField(label="Email")
    contract_number = forms.CharField(label="Номер договора", max_length=20)
    address = forms.CharField(label="Адрес объекта", max_length=255, required=False)
    contract_date = forms.DateField(
        label="Дата заключения договора",
        widget=forms.SelectDateWidget(
            years=range(timezone.now().year - 25, timezone.now().year + 25)
        ),
    )

    class Meta:
        model = CustomUser
        fields = [
            "full_name",
            "phone_number",
            "password",
            "email",
            "service_type",
            "contract_number",
            "contract_date",
            "address",
        ]

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        name_parts = re.split(r"\s+", full_name.strip())

        if len(name_parts) < 2:
            raise forms.ValidationError("Пожалуйста, введите и имя, и фамилию.")

        return full_name

    def save(self, commit=True):
        user = super().save(commit=False)
        full_name = self.cleaned_data["full_name"]

        name_parts = re.split(r"\s+", full_name.strip())
        first_name, last_name = name_parts[0], " ".join(name_parts[1:])

        user.first_name = first_name
        user.last_name = last_name
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()
            Contract.objects.create(
                user=user,
                contract_number=self.cleaned_data["contract_number"],
                service_type=self.cleaned_data["service_type"],
                contract_date=self.cleaned_data["contract_date"],
                address=self.cleaned_data["address"],
            )
        return user


class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(label='Имя Фамилия', max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}))
    service_type = forms.ChoiceField(label='Тип услуги', choices=Contract.ServiceTypeChoices.choices, widget=forms.Select(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label='Номер телефона', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    contract_number = forms.CharField(label='Номер договора', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    contract_date = forms.DateField(label='Дата заключения договора', widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['full_name', 'phone_number', 'password1', 'password2', 'email', 'service_type', 'contract_number', 'contract_date']

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        name_parts = re.split(r'\s+', full_name.strip())

        if len(name_parts) < 2:
            raise forms.ValidationError('Пожалуйста, введите и имя, и фамилию.')

        return full_name

    def save(self, commit=True):
        user = super().save(commit=False)
        full_name = self.cleaned_data['full_name']
        name_parts = re.split(r'\s+', full_name.strip())
        first_name, last_name = name_parts[0], ' '.join(name_parts[1:])

        user.first_name = first_name
        user.last_name = last_name

        if commit:
            user.save()
            Contract.objects.create(
                user=user,
                contract_number=self.cleaned_data['contract_number'],
                service_type=self.cleaned_data['service_type'],
                contract_date=self.cleaned_data['contract_date']
            )
        return user

class CustomUserChangeForm(forms.ModelForm):
    contracts = forms.ModelMultipleChoiceField(queryset=Contract.objects.none(), required=False, widget=forms.SelectMultiple)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'is_active', 'contracts']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['contracts'].queryset = Contract.objects.filter(user=instance)

