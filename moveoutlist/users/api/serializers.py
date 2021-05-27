from django.contrib.auth import get_user_model
from rest_framework import serializers

USER_MODEL = get_user_model()


class UserGetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = ('id', 'first_name', 'last_name')
