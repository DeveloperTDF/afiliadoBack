from rest_framework import generics
from trabajos.api.serializers import TrabajoSerializer
from trabajos.models import Trabajo

class TrabajoList(generics.ListCreateAPIView):
    queryset            =   Trabajo.objects.all()
    serializer_class    =   TrabajoSerializer

class TrabajoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset            =   Trabajo.objects.all()
    serializer_class    =   TrabajoSerializer