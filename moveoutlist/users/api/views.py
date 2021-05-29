from rest_framework import mixins, permissions
from rest_framework.generics import GenericAPIView

from users.api.serializers import UserRegisterSerializer


class RegistrationView(mixins.CreateModelMixin, GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
