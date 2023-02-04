from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions.dono_permission import DonoPermission
from api.serializers.imagem_objeto_serializer import ImagemObjetoSerializer
from api.services import objeto_service
from rest_framework import status as status_http


class ImagemObjetoView(APIView):
    permission_classes = [DonoPermission, ]

    def post(self, request, objeto_id, format=None):
        try:
            objeto = objeto_service.listar_objeto_id(objeto_id)
        except ObjectDoesNotExist:
            return Response(data={"message": "Objeto não encontrado"}, status=status_http.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, objeto)
        imagem_objeto_serializer = ImagemObjetoSerializer(data=request.data)
        if not imagem_objeto_serializer.is_valid():
            return Response(data=imagem_objeto_serializer.errors, status=status_http.HTTP_400_BAD_REQUEST)
        imagem_objeto = imagem_objeto_serializer.validated_data["imagem_objeto"]
        objeto.imagem_objeto = imagem_objeto
        objeto.save()
        return Response(data={"message": "Imagem definida com sucesso!"}, status=status_http.HTTP_200_OK)
