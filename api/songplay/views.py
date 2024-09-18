from rest_framework.viewsets import ModelViewSet
from api.models import SongPlay
from api.songplay.serializers import SongPlaySerializer

class SongPlayApiViewSet(ModelViewSet):
    serializer_class = SongPlaySerializer
    queryset = SongPlay.objects.all()