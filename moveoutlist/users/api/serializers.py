from django.contrib.auth import get_user_model
from rest_framework import serializers

USER_MODEL = get_user_model()


class UserGetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = ('id', 'first_name', 'last_name')


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = ('email', 'password', 'first_name', 'last_name', 'avatar')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = USER_MODEL(**validated_data)
        user.set_password(password)
        user.save()
        return user
