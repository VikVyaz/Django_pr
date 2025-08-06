from django.db import models
from django.utils import timezone

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'Категория "{self.name}"'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['id']
        db_table = 'category'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='photos/', verbose_name='Изображение', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    is_published = models.BooleanField(default=False, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='users', null=True, blank=True,
                              verbose_name='Владелец опубликованного продукта')

    def __str__(self):
        return f'Продукт:{self.name}, категория:{self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['id']
        db_table = 'product'
        permissions = [
            ('can_unpublish_product', 'Может отменять публикацию продукта'),
        ]
