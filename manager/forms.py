import re
from django import forms
from user.models import CustomUser, Contract

class UserCreationForm(forms.ModelForm):
    full_name = forms.CharField(label='Имя Фамилия', max_length=60)
    service_type = forms.ChoiceField(label='Тип услуги', choices=Contract.ServiceTypeChoices.choices)
    phone_number = forms.CharField(label='Номер телефона', max_length=15)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')
    contract_number = forms.CharField(label='Номер договора', max_length=20)
    contract_date = forms.DateField(label='Дата заключения договора', widget=forms.SelectDateWidget)

    class Meta:
        model = CustomUser
        fields = ['full_name', 'phone_number', 'password', 'email', 'service_type', 'contract_number', 'contract_date']

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
        user.set_password(self.cleaned_data['password'])
        
        if commit:
            user.save()
            Contract.objects.create(
                user=user,
                contract_number=self.cleaned_data['contract_number'],
                service_type=self.cleaned_data['service_type'],
                contract_date=self.cleaned_data['contract_date']
            )
        return user
