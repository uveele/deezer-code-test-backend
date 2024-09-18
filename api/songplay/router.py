from rest_framework.routers import DefaultRouter
from api.songplay.views import SongPlayApiViewSet

router_songplays = DefaultRouter()
router_songplays.register(prefix='songplay', basename='songplay', viewset=SongPlayApiViewSet)