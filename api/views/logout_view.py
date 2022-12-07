from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status as status_http


class LogoutView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, format=None):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status_http.HTTP_205_RESET_CONTENT, data={"mensagem": "Logout realizado com sucesso"})
        except Exception as e:
            return Response(data={"message": str(e)}, status=status_http.HTTP_400_BAD_REQUEST)
