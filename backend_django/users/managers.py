from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserRoles(models.TextChoices):
    USER = 'user'
    ADMIN = 'admin'


class UserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, phone, role=UserRoles.USER, password=None):
        if not email:
            raise ValueError('Поле email обязательно к заполнению')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            role=role
        )

        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, role=UserRoles.ADMIN, password=None):
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            role=role
        )
        user.is_active = True
        user.set_password(user.password)
        user.save(using=self._db)

        return user

