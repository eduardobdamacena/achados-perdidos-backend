from django.urls import reverse
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from api.hateoas import Hateoas
from api.models import Local


class LocalSearchResultSerializer(ModelSerializer):
    imagem = SerializerMethodField()
    links = SerializerMethodField(required=False)

    class Meta:
        model = Local
        fields = ("id", "nome", "endereco", "contato", "descricao", "imagem", "links")

    def get_imagem(self, local):
        if local.imagem_local:
            imagem_url = local.imagem_local.url
            return imagem_url
        return None

    def get_links(self, instance):
        links = Hateoas()
        links.add_get("objetos_local", reverse("local-objects", kwargs={'local_id': instance.id}))
        return links.to_array()
