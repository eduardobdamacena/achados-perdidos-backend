from rest_framework.serializers import ModelSerializer
from api.models import Objeto


class EditarObjetoSerializer(ModelSerializer):

    class Meta:
        model = Objeto
        fields = ("nome", "descricao")
