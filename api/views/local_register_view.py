from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status as status_http

from api.permissions.is_post_or_authenticated_permission import IsPostOrAuthenticated
from api.serializers.registrar_local_serializer import RegistrarLocalSerializer


class LocalRegisterView(APIView):
    permission_classes = [IsPostOrAuthenticated]

    def post(self, request, format=None):
        registrar_local_serializer = RegistrarLocalSerializer(data=request.data)
        if registrar_local_serializer.is_valid():
            local_criado = registrar_local_serializer.save()
            registrar_local_serializer = RegistrarLocalSerializer(local_criado)
            return Response(registrar_local_serializer.data, status=status_http.HTTP_201_CREATED)
        return Response(registrar_local_serializer.errors, status=status_http.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        local = request.user.local
        register_local_serializer = RegistrarLocalSerializer(local)
        return Response(register_local_serializer.data, status=status_http.HTTP_200_OK)
