from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from api.models import User


class UsuarioSerializer(ModelSerializer):
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
