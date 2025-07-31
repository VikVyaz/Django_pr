from django.urls import path
from .views import ProductDetailView, ProductListView, ProductCreateView, ContactView, ProductUpdateView, \
    ProductDeleteView, UnpublishProductView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('', ProductListView.as_view(), name='home'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_details'),
    path('new/', ProductCreateView.as_view(), name='to_add_product'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='edit_product'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('product/<int:pk>/unpublish/', UnpublishProductView.as_view(), name='unpublish_product'),
]
