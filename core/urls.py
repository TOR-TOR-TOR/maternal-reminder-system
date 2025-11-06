# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import BaseModelViewSet  # adjust if you have other viewsets

router = DefaultRouter()
# Example: if you add actual models later, you can register them like:
# router.register(r'mymodel', MyModelViewSet, basename='mymodel')

urlpatterns = [
    path('', include(router.urls)),
]
