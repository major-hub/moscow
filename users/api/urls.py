from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.api.views import (
    SmsCreateAPIView,
    CustomUserRegistrationCreateAPIView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sms/', SmsCreateAPIView.as_view(), name='get_sms_code'),
    path('registration/', CustomUserRegistrationCreateAPIView.as_view(), name='registration'),
]
