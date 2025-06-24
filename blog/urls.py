from django.urls import path
from catalog.apps import CatalogConfig
from .views import EntryListView, EntryDetailView, EntryCreateView, EntryUpdateView, EntryDeleteView


app_name = CatalogConfig.name

urlpatterns = [
    path('', EntryListView.as_view(), name='entry_list'),
    path('new/', EntryCreateView.as_view(), name='entry_form'),
    path('entry/<int:pk>', EntryDetailView.as_view(), name='entry_detail'),
    path('entry/<int:pk>/edit/', EntryUpdateView.as_view(), name='entry_edit'),
    path('entry/<int:pk>/delete/', EntryDeleteView.as_view(), name='entry_delete'),
]