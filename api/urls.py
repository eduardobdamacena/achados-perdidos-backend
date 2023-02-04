from django.urls import path

from api.views.imagem_local_view import ImagemLocalView
from api.views.imagem_objeto_view import ImagemObjetoView
from api.views.inicio_view import InicioView
from api.views.local_register_view import LocalRegisterView
from api.views.objeto_view import ObjetoView, ObjetoIDView

urlpatterns = [
    path("", InicioView.as_view(), name="inicio"),
    path("locais", LocalRegisterView.as_view(), name="local-list"),
    path("locais/imagem", ImagemLocalView.as_view(), name="imagem-local-list"),
    path("objetos", ObjetoView.as_view(), name="objeto-list"),
    path("objetos/<int:objeto_id>", ObjetoIDView.as_view(), name="objeto-detail"),
    path("objetos/<int:objeto_id>/imagem", ImagemObjetoView.as_view(), name="imagem-objeto-list"),
]
