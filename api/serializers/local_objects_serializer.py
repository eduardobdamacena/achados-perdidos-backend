from rest_framework.fields import SerializerMethodField, BooleanField
from rest_framework.serializers import ModelSerializer
from api.models import Objeto


class LocalObjectsSerializer(ModelSerializer):
    data_cadastro = SerializerMethodField()
    imagem = SerializerMethodField()
    entregue = BooleanField(read_only=True)

    class Meta:
        model = Objeto
        fields = ("id", "nome", "descricao", "entregue", "data_cadastro", "imagem")

    def get_data_cadastro(self, instance):
        return instance.created_at.strftime("%Y-%m-%d")

    def get_imagem(self, instance):
        request = self.context['request']
        if instance.imagem_objeto:
            imagem_url = instance.imagem_objeto.url
            return request.build_absolute_uri(imagem_url)
        return None
