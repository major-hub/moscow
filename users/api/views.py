from rest_framework.generics import CreateAPIView

from users.api.serializers import (
    EmailSerializer,
    CustomUserRegistrationModelSerializer,
)


class EmailCreateAPIView(CreateAPIView):
    serializer_class = EmailSerializer


class CustomUserRegistrationCreateAPIView(CreateAPIView):
    serializer_class = CustomUserRegistrationModelSerializer
