from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status as status_http, permissions
from api.permissions.dono_permission import DonoPermission
from api.serializers.editar_objeto_serializer import EditarObjetoSerializer
from api.serializers.objeto_serializer import ObjetoSerializer
from api.services import objeto_service
from api.services.objeto_service import listar_objeto_usuario, apagar_objeto


class ObjetoView(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, format=None):
        usuario = request.user
        objetos = listar_objeto_usuario(usuario.id)
        objeto_serializer = ObjetoSerializer(objetos, many=True)
        return Response(data=objeto_serializer.data, status=status_http.HTTP_200_OK)

    def post(self, request, format=None):
        objeto_serializer = ObjetoSerializer(data=request.data, context={'request': request})
        if objeto_serializer.is_valid():
            objeto_serializer.save()
            return Response(objeto_serializer.data, status=status_http.HTTP_201_CREATED)
        return Response(objeto_serializer.errors, status=status_http.HTTP_400_BAD_REQUEST)


class ObjetoIDView(APIView):
    permission_classes = [DonoPermission, ]

    def get(self, request, objeto_id, format=None):
        try:
            objeto = objeto_service.listar_objeto_id(objeto_id)
        except ObjectDoesNotExist:
            return Response(data={"message": "Objeto não encontrado"}, status=status_http.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, objeto)
        objeto_serializer = ObjetoSerializer(objeto)
        return Response(data=objeto_serializer.data, status=status_http.HTTP_200_OK)

    def put(self, request, objeto_id, format=None):
        try:
            objeto = objeto_service.listar_objeto_id(objeto_id)
        except ObjectDoesNotExist:
            return Response(data={"message": "Objeto não encontrado"}, status=status_http.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request, objeto)
        editar_objeto_serializer = EditarObjetoSerializer(objeto, data=request.data)
        if editar_objeto_serializer.is_valid():
            editar_objeto_serializer.save()
            objeto_serializer = ObjetoSerializer(objeto)
            return Response(data=objeto_serializer.data, status=status_http.HTTP_200_OK)
        return Response(editar_objeto_serializer.errors, status=status_http.HTTP_400_BAD_REQUEST)

    def delete(self, request, objeto_id, format=None):
        try:
            objeto = objeto_service.listar_objeto_id(objeto_id)
        except ObjectDoesNotExist:
            return Response(data={"message": "Objeto não encontrado"}, status=status_http.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, objeto)
        apagar_objeto(objeto_id)
        return Response(status=status_http.HTTP_204_NO_CONTENT)
