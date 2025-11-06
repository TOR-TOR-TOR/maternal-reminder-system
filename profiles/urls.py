from rest_framework.routers import DefaultRouter
from django.urls import path, include
from profiles.views import HealthWorkerProfileViewSet, MotherProfileViewSet

router = DefaultRouter()
router.register(r'healthworkers', HealthWorkerProfileViewSet, basename='healthworker')
router.register(r'mothers', MotherProfileViewSet, basename='mother')

urlpatterns = [
    path('', include(router.urls)),
]
