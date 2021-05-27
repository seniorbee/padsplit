from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework.viewsets import ModelViewSet

from places.api.serializers import MoveOutGetSerializer
from places.models import MoveOut
from utils.BaseClasses import MultiSerializerViewSet


class MoveOutViewSet(MultiSerializerViewSet, ModelViewSet):
    serializer_class = MoveOutGetSerializer
    serializers = {}

    def get_queryset(self):
        return MoveOut.objects.select_related('room', 'last_occupant', 'room__address')

    @method_decorator(cache_page(60))
    @method_decorator(vary_on_headers('Accept-Language'))
    def dispatch(self, request, *args, **kwargs):
        return super(MoveOutViewSet, self).dispatch(request, *args, **kwargs)
