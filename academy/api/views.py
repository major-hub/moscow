from rest_framework.generics import ListAPIView, RetrieveAPIView

from academy.models import Rectorate, Faculty, Department
from academy.api.serializers import (
    RectorateModelSerializer,
    FacultyListModelSerializer,
    DepartmentModelSerializer,
    FacultyDetailModelSerializer,
)


class RectorateListAPIView(ListAPIView):
    queryset = Rectorate.objects.all()
    serializer_class = RectorateModelSerializer


class FacultyListAPIView(ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultyListModelSerializer


class FacultyRetrieveAPIView(RetrieveAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultyDetailModelSerializer


class DepartmentRetrieveAPIView(RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentModelSerializer
