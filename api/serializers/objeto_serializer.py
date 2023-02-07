from django.urls import reverse
from rest_framework.fields import SerializerMethodField, BooleanField
from rest_framework.serializers import ModelSerializer

from api.hateoas import Hateoas
from api.models import Objeto


class ObjetoSerializer(ModelSerializer):
    data_cadastro = SerializerMethodField()
    imagem = SerializerMethodField()
    entregue = BooleanField(read_only=True)
    links = SerializerMethodField(required=False)

    class Meta:
        model = Objeto
        fields = ("id", "nome", "descricao", "entregue", "data_cadastro", "imagem", "links")

    def get_data_cadastro(self, instance):
        return instance.created_at.strftime("%Y-%m-%d")

    def get_imagem(self, instance):
        if instance.imagem_objeto:
            imagem_url = instance.imagem_objeto.url
            return imagem_url
        return None

    def create(self, validated_data):
        local_id = self.context['request'].user.local.id
        objeto = Objeto.objects.create(local_id=local_id, **validated_data)
        return objeto

    def get_links(self, instance):
        links = Hateoas()
        links.add_get("self", reverse("objeto-detail", kwargs={'objeto_id': instance.id}))
        links.add_put("atualizar_objeto", reverse("objeto-detail", kwargs={'objeto_id': instance.id}))
        links.add_delete("apagar_objeto", reverse("objeto-detail", kwargs={'objeto_id': instance.id}))
        links.add_post("definir_imagem_objeto", reverse("imagem-objeto-detail", kwargs={'objeto_id': instance.id}))
        return links.to_array()
