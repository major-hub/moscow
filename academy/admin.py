from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableStackedInline, TranslatableTabularInline

from .models import (
    Rectorate, Faculty, FacultyAdministration, FacultyMaster, FacultyBachelor, Department, DepartmentSubject,
    DepartmentStaff
)


class FacultyAdministrationInline(TranslatableStackedInline):
    model = FacultyAdministration
    extra = 1


class FacultyBachelorInline(TranslatableTabularInline):
    model = FacultyBachelor
    extra = 1


class FacultyMasterInline(TranslatableTabularInline):
    model = FacultyMaster
    extra = 1


@admin.register(Rectorate)
class RectorateAdmin(TranslatableAdmin):
    pass


@admin.register(Faculty)
class FacultyAdmin(TranslatableAdmin):
    inlines = [FacultyAdministrationInline, FacultyBachelorInline, FacultyMasterInline]


class DepartmentSubjectInline(TranslatableTabularInline):
    model = DepartmentSubject
    extra = 1


class DepartmentStaffInline(TranslatableTabularInline):
    model = DepartmentStaff
    extra = 1


@admin.register(Department)
class DepartmentAdmin(TranslatableAdmin):
    inlines = [DepartmentSubjectInline, DepartmentStaffInline]
