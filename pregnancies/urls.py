from rest_framework.routers import DefaultRouter
from .views import PregnancyViewSet

router = DefaultRouter()
router.register(r'pregnancies', PregnancyViewSet, basename='pregnancy')

urlpatterns = router.urls