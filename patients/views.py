# Create your views here.
from rest_framework import generics
from .models import Patient
from .serializers import PatientSerializer

# List all patients or create a new patient
class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# Retrieve, update, or delete a single patient
class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
