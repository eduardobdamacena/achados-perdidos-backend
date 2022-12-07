from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status as status_http

from api.models import Local
from api.serializers.imagem_local_serializer import ImagemLocalSerializer


class ImagemLocalView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        imagem_local_serializer = ImagemLocalSerializer(data=request.data)
        if not imagem_local_serializer.is_valid():
            return Response(data=imagem_local_serializer.errors, status=status_http.HTTP_400_BAD_REQUEST)

        imagem_local = imagem_local_serializer.validated_data["imagem_local"]
        user = request.user
        local = user.local
        local.imagem_local = imagem_local
        local.save()
        return Response(data={"message": "Imagem atualizada com sucesso"}, status=status_http.HTTP_200_OK)
