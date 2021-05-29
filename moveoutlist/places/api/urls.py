from rest_framework.routers import DefaultRouter

from places.api.views import MoveOutViewSet

app_name = 'places'

router = DefaultRouter()
router.register(r'move-outs', viewset=MoveOutViewSet, basename='move-outs')

urlpatterns = router.urls
