from django.contrib.auth.hashers import make_password
from django.urls import reverse
from rest_framework.fields import CharField, SerializerMethodField, ImageField
from rest_framework.serializers import ModelSerializer
from api.hateoas import Hateoas
from api.models import Local, User
from api.serializers.usuario_serializer import UsuarioSerializer


class LocalSerializer(ModelSerializer):
    nome = CharField(min_length=3)
    endereco = CharField(min_length=3)
    contato = CharField(min_length=3)
    descricao = CharField(max_length=255, allow_blank=True, allow_null=True)
    imagem = SerializerMethodField()
    usuario = UsuarioSerializer()
    links = SerializerMethodField(required=False)

    class Meta:
        model = Local
        exclude = ["imagem_local"]

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario_data['password'] = make_password(usuario_data['password'])
        usuario_data.pop('password_confirmation', None)
        usuario_criado = User.objects.create(**usuario_data)

        local_criado = Local.objects.create(**validated_data, usuario=usuario_criado)

        return local_criado

    def get_imagem(self, local):
        if local.imagem_local:
            imagem_url = local.imagem_local.url
            return imagem_url
        return None

    def get_links(self, local):
        links = Hateoas()
        links.add_get("self", reverse("local-list"))
        links.add_post("definir_imagem_local", reverse("imagem-local-list"))
        links.add_get("listar_objetos_local", reverse("objeto-list"))
        links.add_post("adicionar_objeto_local", reverse("objeto-list"))
        return links.to_array()
