from random import randint

from django.core.cache import cache
from rest_framework import serializers
from django.core.mail.message import EmailMessage

from users.models import CustomUser


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ['email']

    @staticmethod
    def send_mail(code: str, to: list):
        email = EmailMessage(subject='Confirmation code of Moscow Academy', body=code, to=to)
        return email.send()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        code = str(randint(10000, 99999))
        email = validated_data['email']

        if self.send_mail(code, [email]):
            if CustomUser.objects.filter(email=email).exists():
                user = CustomUser.objects.get(email=email)
                user.set_password(code)
                user.save()
                created = False
            else:
                cache.set(email, code, 3600)
                created = True
            return {
                "success": True,
                "created": created,
                "message": "Confirmation code is sent to your email"
            }
        else:
            return {
                "success": False,
                "created": False,
                "message": "Please, check your email"
            }

    def to_representation(self, instance):
        return instance


class CustomUserRegistrationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'password',
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone_number': {'required': True},
        }

    def validate(self, attrs):
        data = super().validate(attrs)
        code = cache.get(data['email'])
        if code:
            if code == data['password']:
                return data
        raise serializers.ValidationError({'password': 'Incorrect code'})

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
