from rest_framework.fields import ImageField
from rest_framework.serializers import Serializer


class ImagemLocalSerializer(Serializer):
    imagem_local = ImageField(required=True)
