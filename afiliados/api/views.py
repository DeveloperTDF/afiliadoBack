from rest_framework import generics
from afiliados.api.serializers import AfiliadoSerializer
from afiliados.models import Afiliado

class AfiliadoList(generics.ListCreateAPIView):
    queryset            =   Afiliado.objects.all()
    serializer_class    =   AfiliadoSerializer

class AfiliadoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset            =   Afiliado.objects.all()
    serializer_class    =   AfiliadoSerializer