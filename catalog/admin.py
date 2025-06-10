from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', 'description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'category', 'price', 'created_at', 'updated_at',)
    list_filter = ('category', 'created_at', 'updated_at',)
    search_fields = ('name', 'description',)


