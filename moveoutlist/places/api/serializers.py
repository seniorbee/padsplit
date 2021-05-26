from rest_framework import serializers

from places.models import MoveOut


class MoveOutGetSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for getting move out data"""
    address = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    uid = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()

    class Meta:
        model = MoveOut
        fields = ('move_out_date', 'id', 'address', 'room', 'location', 'last_occupant', 'balance')
