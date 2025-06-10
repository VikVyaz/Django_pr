from django.urls import path
from . import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', views.contacts, name='contacts'),
]
