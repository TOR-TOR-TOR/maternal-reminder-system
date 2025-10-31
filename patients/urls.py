from django.urls import path
from .views import PatientListCreateView, PatientDetailView

app_name = 'patients'
urlpatterns = [
    path('', PatientListCreateView.as_view(), name='patients-list'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patients-detail'),
]
