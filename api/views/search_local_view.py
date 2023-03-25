from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status as status_http
from api.serializers.local_search_result_serializer import LocalSearchResultSerializer
from api.services import local_service


class SearchLocalView(APIView):

    def get(self, request, format=None):
        local_name = request.query_params.get("nome", None)
        if not local_name:
            return Response(data={"message": "Digite um nome para buscar o local"},
                            status=status_http.HTTP_400_BAD_REQUEST)
        list_local = local_service.search_by_name(local_name)
        local_search_result_serializer = LocalSearchResultSerializer(list_local, many=True, context={"request": request})
        return Response(data=local_search_result_serializer.data, status=status_http.HTTP_200_OK)
