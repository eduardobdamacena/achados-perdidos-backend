from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from api.permissions.dono_permission import DonoPermission
from api.serializers.dono_objeto_serializer import DonoObjetoSerializer
from api.services import objeto_service
from rest_framework import status as status_http


class DonoObjetoView(APIView):
    permission_classes = [DonoPermission, ]

    def post(self, request, objeto_id, format=None):
        try:
            objeto = objeto_service.listar_objeto_id(objeto_id)
        except ObjectDoesNotExist:
            return Response(data={"message": "Objeto não encontrado"}, status=status_http.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, objeto)
        dono_objeto_serializer = DonoObjetoSerializer(objeto, data=request.data)
        if dono_objeto_serializer.is_valid():
            dono_objeto_serializer.save()
            return Response(data={"mensagem": "Dono do objeto definido com sucesso"}, status=status_http.HTTP_200_OK)
        else:
            return Response(dono_objeto_serializer.errors, status=status_http.HTTP_400_BAD_REQUEST)
