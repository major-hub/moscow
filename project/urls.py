from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/academy/', include('academy.api.urls')),
    path('api/users/', include('users.api.urls')),
]
