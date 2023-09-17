from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from apps.users.managers import CustomUserManager


class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    date_of_birth = models.DateTimeField(null=True)
    username = None

    objects = CustomUserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
