import random

from rest_framework import serializers

from places.models import MoveOut, Address


class AddressGetSerializer(serializers.ModelSerializer):
    """Serializer for showing address data in Move-out list"""

    class Meta:
        model = Address
        fields = ('id', 'title', 'location')


class MoveOutGetSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for getting move out data"""
    address = AddressGetSerializer(source='room.address')
    location = serializers.SerializerMethodField()
    uid = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()

    class Meta:
        model = MoveOut
        fields = ('move_out_date', 'id', 'address', 'room', 'location', 'last_occupant', 'uid', 'balance')

    def get_location(self, obj: MoveOut):
        return obj.room.address.location

    def get_uid(self, obj: MoveOut):
        return obj.last_occupant_id

    def get_balance(self, obj: MoveOut):
        return random.randint(0, 500)
