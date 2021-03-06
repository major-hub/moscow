from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.throttling import AnonRateThrottle

from posts.api.paginations import Pagination6, Pagination24
from posts.models import Gallery, News
from posts.api.serializers import (
    GalleryModelSerializer,
    NewsModelSerializer, QuestionModelSerializer, ContactModelSerializer,
)


class GalleryListAPIView(ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GalleryModelSerializer
    pagination_class = Pagination24


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsModelSerializer
    pagination_class = Pagination6

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class QuestionCreateAPIView(CreateAPIView):
    serializer_class = QuestionModelSerializer
    throttle_classes = [AnonRateThrottle]


class ContactCreateAPIView(CreateAPIView):
    serializer_class = ContactModelSerializer
    throttle_classes = [AnonRateThrottle]
