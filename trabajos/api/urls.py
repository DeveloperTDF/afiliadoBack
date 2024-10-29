from django.urls import path
from trabajos.api.views import TrabajoList,TrabajoDetail

urlpatterns =   [
    path('', TrabajoList.as_view(), name='list'),
    path('<int:pk>', TrabajoDetail.as_view(), name='Detail'),
]
