from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from .managers import UserManager, UserRoles
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=70, validators=[MinLengthValidator(1)], verbose_name='Имя')
    last_name = models.CharField(max_length=70, validators=[MinLengthValidator(1)], verbose_name='Фамилия')
    phone = PhoneNumberField(max_length=130, validators=[MinLengthValidator(1)], verbose_name='Номер телефона')
    email = models.EmailField(max_length=255, validators=[MinLengthValidator(1)], unique=True, verbose_name='Электронный адрес')
    role = models.CharField(max_length=6, choices=UserRoles.choices, default=UserRoles.USER, verbose_name='Роль')
    image = models.ImageField(verbose_name='Аватар', null=True, blank=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


