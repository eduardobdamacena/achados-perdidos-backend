from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from api.hateoas import Hateoas
from rest_framework import status as status_http


class InicioView(APIView):
    def get(self, request, format=None):
        links = Hateoas()
        links.add_post("login", reverse("token_obtain_pair"))
        links.add_post("register", reverse("local-list"))
        links.add_post("logout", reverse("token_logout"))
        links.add_post("refresh_token", reverse("token_refresh"))

        return Response(data={"links": links.to_array()}, status=status_http.HTTP_200_OK)
