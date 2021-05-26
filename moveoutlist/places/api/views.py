from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from places.api.serializers import MoveOutGetSerializer
from places.models import MoveOut


class MoveOutViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, GenericViewSet):
    serializer_class = MoveOutGetSerializer

    def get_queryset(self):
        return MoveOut.objects.all()
