from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    email = models.EmailField(verbose_name='Email', unique=True)
    phone_number = PhoneNumberField(verbose_name='Номер телефона', max_length=15, blank=True, null=True)
    avatar = models.ImageField(verbose_name='Аватар', upload_to='avatars/', blank=True, null=True)
    country = CountryField(blank_label='Выберите страну', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователь'

    def __str__(self):
        return self.username
