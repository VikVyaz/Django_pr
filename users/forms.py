from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.modelfields import PhoneNumberField

from catalog.forms import StyleFormMixin
from .models import User


class UserRegisterFrom(StyleFormMixin, UserCreationForm):
    phone_number = PhoneNumberField(verbose_name='Номер телефона', max_length=15, blank=True, null=True)
    usable_password = None

    placeholder_data = {
        'email': 'Email пользователя',
        'password': 'Пароль пользователя'
    }

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
