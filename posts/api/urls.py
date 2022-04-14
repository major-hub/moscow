from django.urls import path

from posts.api.views import (
    GalleryListAPIView,
    NewsListAPIView,
    QuestionCreateAPIView,
    ContactCreateAPIView,
)

urlpatterns = [
    path('gallery/', GalleryListAPIView.as_view(), name='gallery'),
    path('news/', NewsListAPIView.as_view(), name='news'),
    path('question/', QuestionCreateAPIView.as_view(), name='question_create'),
    path('contact/', ContactCreateAPIView.as_view(), name='contact_create'),
]
