from rest_framework import serializers

from parler_rest.fields import TranslatedFieldsField
from parler_rest.serializers import TranslatableModelSerializer

from .mixins import TranslatedSerializerMixin
from ..models import Gallery, News, Question, Contact


class GalleryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['image']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return rep['image']


class NewsModelSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=News)

    class Meta:
        model = News
        fields = (
            'translations',
            'image',
            'created_at',
        )


class QuestionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'name',
            'phone_number',
            'message',
        )


class ContactModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'name',
            'phone_number',
        )
