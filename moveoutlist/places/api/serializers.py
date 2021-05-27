import random

from rest_framework import serializers

from places.models import MoveOut, Address
from users.api.serializers import UserGetSerializer


class AddressGetSerializer(serializers.ModelSerializer):
    """Serializer for showing address data """

    class Meta:
        model = Address
        fields = ('id', 'title', 'location')


class MoveOutCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating an address object"""

    class Meta:
        model = MoveOut
        fields = ('move_out_date', 'room', 'last_occupant')


class MoveOutGetSerializer(serializers.ModelSerializer):
    """Serializer for getting move out data"""
    address = AddressGetSerializer(source='room.address')
    uid = serializers.ReadOnlyField(source='last_occupant_id')
    balance = serializers.ReadOnlyField(default='$ 405.90')
    room = serializers.UUIDField()
    last_occupant = UserGetSerializer()

    class Meta:
        model = MoveOut
        fields = ('id', 'move_out_date', 'address',
                  'room', 'last_occupant', 'uid', 'balance')
