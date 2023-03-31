from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from api.models import Objeto


class DonoObjetoSerializer(ModelSerializer):
    dono_nome = CharField(required=True, min_length=3, max_length=255, allow_null=False, allow_blank=False)

    class Meta:
        model = Objeto
        fields = ("dono_nome", "dono_cpf")
        extra_kwargs = {"dono_cpf": {"required": True, "allow_null": False, "allow_blank": False}}

    def update(self, instance, validated_data):
        instance.entregue = True
        instance.dono_nome = validated_data["dono_nome"]
        instance.dono_cpf = validated_data["dono_cpf"]
        instance.save()
        return instance
