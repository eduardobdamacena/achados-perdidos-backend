from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status as status_http
from api.serializers.local_objects_serializer import LocalObjectsSerializer
from api.services import objeto_service, local_service


class LocalObjectsView(APIView):

    def get(self, request, local_id, format=None):
        try:
            local = local_service.listar_local_id(local_id)
        except ObjectDoesNotExist:
            return Response(data={"message": "Local não encontrado"}, status=status_http.HTTP_404_NOT_FOUND)
        objects = objeto_service.listar_objetos_local_nao_entregue(local_id)
        local_object_serializer = LocalObjectsSerializer(objects, many=True, context={"request": request})
        return Response(data=local_object_serializer.data, status=status_http.HTTP_200_OK)
