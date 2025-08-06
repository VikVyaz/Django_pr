from django.core.cache import cache

from config.settings import CACHE_ENABLE

from .models import Category, Product


def get_products_from_cache():
    """Получение продуктов из кэша, если пуст, берется из БД"""

    if not CACHE_ENABLE:
        return Product.objects.all()

    key = 'product_list'
    products = cache.get(key)

    if products is not None:
        return products

    products = Product.objects.all()
    cache.set(key, products, 60 * 15)
    return products


def get_products_by_category(category_name):
    """Фильтрация продуктов согласно заданной категории"""

    category = Category.objects.get(name=category_name)
    filtered_products = get_products_from_cache().filter(category=category)

    return filtered_products
