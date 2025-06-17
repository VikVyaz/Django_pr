from django.urls import path
from . import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', views.contacts, name='contacts'),
    path('products/<int:product_id>', views.product_details, name='product_details'),
    path('to_add_product/', views.to_add_product, name='to_add_product'),
]
