from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, email, password=None, **extra_fields):
        if not phone_number:
            raise ValueError(_('Номер телефона должен быть указан'))
        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        return self.create_user(phone_number, email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None  # Отключение поля username
    phone_number = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number
    
    
class Contract(models.Model):
    class ServiceTypeChoices(models.IntegerChoices):
        APARTMENT_REPLANNING = 1, 'Перепланировка квартиры'
        RESIDENTIAL_REPLANNING = 2, 'Перепланировка жилых помещений'
        NON_RESIDENTIAL_REPLANNING = 3, 'Перепланировка нежилого здания'
        CADASTRAL_WORK = 4, 'Кадастровые работы'
    
    class StatusTypeChoices(models.IntegerChoices):
        PHASE1 = 1, '1 этап'
        PHASE2 = 2, '2 этап'
        PHASE3 = 3, '3 этап'
        PHASE4 = 4, '4 этап'
        PHASE5 = 5, '5 этап'
        PHASE6 = 6, '6 этап'
        Done = 0, 'Завершен'

    user = models.ForeignKey(CustomUser, related_name='contracts', on_delete=models.CASCADE)
    contract_number = models.CharField(max_length=20, unique=True)
    service_type = models.IntegerField(choices=ServiceTypeChoices.choices,)
    status = models.IntegerField(choices=StatusTypeChoices.choices, default=StatusTypeChoices.PHASE1)
    contract_date = models.DateField()
    completion_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def max_phases(self):
        if self.service_type == self.ServiceTypeChoices.CADASTRAL_WORK:
            return self.StatusTypeChoices.PHASE3
        else:
            return self.StatusTypeChoices.PHASE6
        
    def next_phase(self):
        if self.service_type == self.ServiceTypeChoices.CADASTRAL_WORK:
            if self.status < self.StatusTypeChoices.PHASE3:
                self.status += 1
                self.save()
        else:
            if self.status < self.StatusTypeChoices.PHASE6:
                self.status += 1
                self.save()

    def last_phase(self):
        if self.service_type == self.ServiceTypeChoices.CADASTRAL_WORK:
            if self.status == self.StatusTypeChoices.PHASE3:
                return 3
        else:
            if self.status == self.StatusTypeChoices.PHASE6:
                return 6
        return False
    
    def complete_project(self):
        if self.is_last_phase():
            self.status = self.StatusTypeChoices.Done
            self.completion_date = timezone.now()
            self.save()
    
    def is_done(self):
        return self.status == self.StatusTypeChoices.Done
    
    def __str__(self):
        return self.contract_number
