from django.urls import path

from api.views.imagem_local_view import ImagemLocalView
from api.views.inicio_view import InicioView
from api.views.local_register_view import LocalRegisterView

urlpatterns = [
    path("", InicioView.as_view(), name="inicio"),
    path("locais", LocalRegisterView.as_view(), name="local-list"),
    path("locais/imagem", ImagemLocalView.as_view(), name="imagem-local-list")
]
