from django.urls import path

from academy.api.views import (
    RectorateListAPIView,
    FacultyListAPIView,
    FacultyRetrieveAPIView,
    DepartmentRetrieveAPIView,
)

urlpatterns = [
    path('rectorate/', RectorateListAPIView.as_view(), name='rectorate'),
    path('faculty/', FacultyListAPIView.as_view(), name='faculty'),
    path('faculty/<int:pk>/', FacultyRetrieveAPIView.as_view(), name='faculty_detail'),
    path('department/<int:pk>/', DepartmentRetrieveAPIView.as_view(), name='department_detail'),
]
