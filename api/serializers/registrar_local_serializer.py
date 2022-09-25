from django.contrib.auth.hashers import make_password
from django.urls import reverse
from rest_framework.fields import CharField, SerializerMethodField
from rest_framework.serializers import ModelSerializer

from api.hateoas import Hateoas
from api.models import Local, User
from api.serializers.usuario_serializer import UsuarioSerializer


class RegistrarLocalSerializer(ModelSerializer):
    nome = CharField(min_length=3)
    endereco = CharField(min_length=3)
    contato = CharField(min_length=3)
    descricao = CharField(max_length=255)
    usuario = UsuarioSerializer()
    links = SerializerMethodField(required=False)

    class Meta:
        model = Local
        fields = '__all__'

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario_data['password'] = make_password(usuario_data['password'])
        usuario_data.pop('password_confirmation', None)
        usuario_criado = User.objects.create(**usuario_data)

        local_criado = Local.objects.create(**validated_data, usuario=usuario_criado)

        return local_criado

    def get_links(self, local):
        links = Hateoas()
        links.add_get("self", reverse("local-list"))
        links.add_post("definir_imagem_local", reverse("imagem-local-list"))
        return links.to_array()
