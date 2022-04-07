from django.urls import path

from posts.api.views import (
    GalleryListAPIView,
    NewsListAPIView,
)

urlpatterns = [
    path('gallery/', GalleryListAPIView.as_view(), name='gallery'),
    path('news/', NewsListAPIView.as_view(), name='news'),
]
