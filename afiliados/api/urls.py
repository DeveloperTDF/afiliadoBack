from django.urls import path
from afiliados.api.views import AfiliadoList, AfiliadoDetail

urlpatterns =   [
    path('', AfiliadoList.as_view(), name='list'),
    path('<int:pk>', AfiliadoDetail.as_view(), name='Detail'),
]
