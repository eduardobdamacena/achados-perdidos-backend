from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status as status_http
from api.permissions.is_post_or_authenticated_permission import IsPostOrAuthenticated
from api.serializers.editar_local_serializer import EditarLocalSerializer
from api.serializers.local_serializer import LocalSerializer


class LocalRegisterView(APIView):
    permission_classes = [IsPostOrAuthenticated]

    def post(self, request, format=None):
        local_serializer = LocalSerializer(data=request.data, context={"request": request})
        if local_serializer.is_valid():
            local_criado = local_serializer.save()
            local_serializer = LocalSerializer(local_criado, context={"request": request})
            return Response(local_serializer.data, status=status_http.HTTP_201_CREATED)
        return Response(local_serializer.errors, status=status_http.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        local = request.user.local
        register_local_serializer = LocalSerializer(local, context={"request": request})
        return Response(register_local_serializer.data, status=status_http.HTTP_200_OK)

    def put(self, request, format=None):
        local = request.user.local
        editar_local_serializer = EditarLocalSerializer(local, data=request.data, context={"request": request})
        if editar_local_serializer.is_valid():
            local_atualizado = editar_local_serializer.save()
            local_serializer = LocalSerializer(local_atualizado, context={"request": request})
            return Response(data=local_serializer.data, status=status_http.HTTP_200_OK)
        return Response(editar_local_serializer.errors, status=status_http.HTTP_400_BAD_REQUEST)
