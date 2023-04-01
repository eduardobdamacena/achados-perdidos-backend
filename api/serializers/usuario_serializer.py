from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, EmailField
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from api.models import User


class UsuarioSerializer(ModelSerializer):
    email = EmailField()
    password_confirmation = CharField(write_only=True, required=True)
    password = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("id", "nome", "email", 'password', 'password_confirmation')

    def validate_password(self, password):
        password_confirmation = None
        if getattr(self, "initial_data", None):
            # for a case when serializer used DIRECTLY
            password_confirmation = self.initial_data.get("password_confirmation")
        else:
            # for a case when serializer used NESTED
            password_confirmation = self.parent.initial_data["usuario"]["password_confirmation"]
        if password != password_confirmation:
            raise ValidationError("Senhas não combinam")
        return password

    def validate_email(self, value):
        if self.context['request'].method == 'POST':
            if self.Meta.model.objects.filter(email=value).exists():
                raise ValidationError('usuário com este email já existe.')
        elif self.context['request'].method == 'PUT':
            user = self.Meta.model.objects.filter(email=value).first()
            if user and user.id != self.context['request'].user.id:
                raise ValidationError('usuário com este email já existe.')
        return value
