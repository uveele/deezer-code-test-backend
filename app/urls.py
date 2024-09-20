from django.contrib import admin
from django.urls import path, include
from .views import main_dashboard
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main_dashboard, name='main_dashboard')
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
