from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status as status_http
from api.serializers.local_objects_serializer import LocalObjectsSerializer
from api.services import objeto_service


class LocalObjectsView(APIView):

    def get(self, request, local_id, format=None):
        objects = objeto_service.listar_objetos_local(local_id)
        local_object_serializer = LocalObjectsSerializer(objects, many=True, context={"request": request})
        return Response(data=local_object_serializer.data, status=status_http.HTTP_200_OK)
