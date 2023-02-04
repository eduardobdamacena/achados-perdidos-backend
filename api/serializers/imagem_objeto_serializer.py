from rest_framework.fields import ImageField
from rest_framework.serializers import Serializer


class ImagemObjetoSerializer(Serializer):
    imagem_objeto = ImageField(required=True)
