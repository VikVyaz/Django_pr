from django.contrib import admin
from django.urls import path, include
from catalog.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),  # <--Для постановки home.html как домашняя страница
    path('', include('catalog.urls', namespace='catalog')),
]
