from rest_framework.viewsets import ModelViewSet
from api.models import Search
from api.search.serializers import SearchSerializer

class SearchApiViewSet(ModelViewSet):
    serializer_class = SearchSerializer
    queryset = Search.objects.all()