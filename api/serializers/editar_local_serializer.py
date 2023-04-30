from django.contrib.auth.hashers import make_password
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from api.models import Local
from api.serializers.editar_usuario_serializer import EditarUsuarioSerializer


class EditarLocalSerializer(ModelSerializer):
    nome = CharField(min_length=3)
    endereco = CharField(min_length=3)
    contato = CharField(min_length=3)
    descricao = CharField(max_length=255, allow_blank=True, allow_null=True)
    usuario = EditarUsuarioSerializer()

    class Meta:
        model = Local
        exclude = ["imagem_local"]

    def update(self, instance, validated_data):
        usuario_data = validated_data.pop('usuario')
        if "password" in usuario_data:
            usuario_data['password'] = make_password(usuario_data['password'])
            usuario_data.pop('password_confirmation', None)
        editar_usuario_serializer = EditarUsuarioSerializer()
        super(self.__class__, self).update(instance, validated_data)
        super(EditarUsuarioSerializer, editar_usuario_serializer).update(instance.usuario, usuario_data)
        return instance
