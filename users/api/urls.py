from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.api.views import (
    EmailCreateAPIView,
    CustomUserRegistrationCreateAPIView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('email/', EmailCreateAPIView.as_view(), name='get_email_code'),
    path('registration/', CustomUserRegistrationCreateAPIView.as_view(), name='registration'),
]
