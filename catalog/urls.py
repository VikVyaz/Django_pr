from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig

from .views import (ContactView, ProductCreateView, ProductDeleteView,
                    ProductDetailView, ProductListView,
                    ProductsByCategoryListView, ProductUpdateView,
                    UnpublishProductView)

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('', ProductListView.as_view(), name='home'),
    path('category/<int:pk>', ProductsByCategoryListView.as_view(), name='products_by_category'),
    path('product/<int:pk>', cache_page(60, key_prefix='product_details')(ProductDetailView.as_view()),
         name='product_details'),
    path('new/', ProductCreateView.as_view(), name='to_add_product'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='edit_product'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('product/<int:pk>/unpublish/', UnpublishProductView.as_view(), name='unpublish_product'),
]
