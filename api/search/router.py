from rest_framework.routers import DefaultRouter
from api.search.views import SearchApiViewSet

router_searches = DefaultRouter()
router_searches.register(prefix='search', basename='search', viewset=SearchApiViewSet)