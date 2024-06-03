from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

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
    class Status(models.IntegerChoices):
       PHASE1 = 1
       PHASE2 = 2
       PHASE3 = 3
       PHASE4 = 4
       PHASE5 = 5
       PHASE6 = 6
       DONE = 0
       
    user = models.ForeignKey(CustomUser, related_name='contracts', on_delete=models.CASCADE)
    contract_number = models.CharField(max_length=20, unique=True)
    service_type = models.CharField(max_length=50)
    contract_date = models.DateField()
    completion_date = models.DateField(null=True, blank=True)
    status = models.IntegerField(choices=Status)

    def __str__(self):
        return self.contract_number