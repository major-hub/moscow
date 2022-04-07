from random import randint

from django.core.cache import cache
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from users.api.sms import eskiz_send_message
from users.models import CustomUser


class SmsSerializer(serializers.Serializer):
    username = serializers.CharField()

    class Meta:
        fields = ['username']

    @staticmethod
    def validate_username(username: str):
        ph = username.replace(' ', '').replace('+', '')
        if not bool(ph.isdigit() and ph.startswith('998') and len(ph) == 12):
            raise serializers.ValidationError('Phone number must be like 998911144735')
        return ph

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        code = str(randint(10000, 99999))
        username = validated_data['username']

        res = eskiz_send_message(username, code)
        user = CustomUser.objects.filter(username=username)

        if res.status_code == 200:
            if user.exists():
                user.update(password=code)
                created = False
            else:
                cache.set(username, code, 3600)
                created = True
            return {
                "success": True,
                "created": created,
                "message": "Confirmation code is sent to your phone number"
            }
        else:
            return {
                "success": False,
                "created": False,
                "message": "Please, check your phone number",
                "error": res.json()
            }

    def to_representation(self, instance):
        return instance


class CustomUserRegistrationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'password',
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    @staticmethod
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def validate(self, attrs):
        data = super().validate(attrs)
        code = cache.get(data['username'])
        if code and code == data['password']:
            return data
        raise serializers.ValidationError({'password': 'Incorrect code'})

    def to_representation(self, instance):
        return self.get_tokens_for_user(instance)
