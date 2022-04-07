from rest_framework.generics import CreateAPIView

from users.api.serializers import (
    SmsSerializer,
    CustomUserRegistrationModelSerializer,
)


class SmsCreateAPIView(CreateAPIView):
    serializer_class = SmsSerializer


class CustomUserRegistrationCreateAPIView(CreateAPIView):
    serializer_class = CustomUserRegistrationModelSerializer
