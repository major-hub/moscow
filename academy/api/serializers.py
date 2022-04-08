from parler_rest.fields import TranslatedFieldsField
from parler_rest.serializers import TranslatableModelSerializer
from rest_framework import serializers

from posts.api.mixins import TranslatedSerializerMixin
from academy.models import Rectorate, FacultyAdministration, FacultyBachelor, FacultyMaster, Faculty, DepartmentSubject, \
    DepartmentStaff, Department


class RectorateModelSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Rectorate)

    class Meta:
        model = Rectorate
        fields = (
            'translations',
            'image',
            'phone_number',
            'email',
            'instagram',
            'telegram',
            'facebook',
        )


class FacultyAdministrationModelSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=FacultyAdministration)

    class Meta:
        model = FacultyAdministration
        fields = (
            'translations',
            'image',
            'phone_number',
            'email',
            'instagram',
            'telegram',
            'facebook',
        )


class FacultyBachelorModelSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=FacultyBachelor)

    class Meta:
        model = FacultyBachelor
        fields = (
            'translations',
            'code',
        )


class FacultyMasterModelSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=FacultyMaster)

    class Meta:
        model = FacultyMaster
        fields = (
            'translations',
            'code',
        )


class DepartmentNameModelSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Department)

    class Meta:
        model = Department
        fields = ['id', 'translations']


class FacultyListModelSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Faculty)
    department = serializers.SerializerMethodField()

    def get_department(self, obj):
        instance = obj.department_set.all()
        return DepartmentNameModelSerializer(instance, many=True, context=self.context).data

    class Meta:
        model = Faculty
        fields = (
            'translations',
            'id',

            # serializer fields
            'department',
        )


class FacultyDetailModelSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Faculty)
    administration = serializers.SerializerMethodField()
    bachelor = serializers.SerializerMethodField()
    master = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()

    def get_administration(self, obj):
        instance = obj.facultyadministration_set.all()
        return FacultyAdministrationModelSerializer(instance, many=True, context=self.context).data

    def get_bachelor(self, obj):
        instance = obj.facultybachelor_set.all()
        return FacultyBachelorModelSerializer(instance, many=True, context=self.context).data

    def get_master(self, obj):
        instance = obj.facultymaster_set.all()
        return FacultyMasterModelSerializer(instance, many=True, context=self.context).data

    def get_department(self, obj):
        instance = obj.department_set.all()
        return DepartmentNameModelSerializer(instance, many=True, context=self.context).data

    class Meta:
        model = Faculty
        fields = (
            'translations',
            'id',
            'image',

            # serializer fields
            'administration',
            'bachelor',
            'master',
            'department',
        )


class DepartmentSubjectModelSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=DepartmentSubject)

    class Meta:
        model = DepartmentSubject
        fields = (
            'translations',
            'degree',
        )


class DepartmentStaffModelSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=DepartmentStaff)

    class Meta:
        model = DepartmentStaff
        fields = ['translations']


class DepartmentModelSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Department)
    subject = serializers.SerializerMethodField()
    staff = serializers.SerializerMethodField()

    def get_subject(self, obj):
        instance = obj.departmentsubject_set.all()
        return DepartmentStaffModelSerializer(instance, many=True, context=self.context).data

    def get_staff(self, obj):
        instance = obj.departmentstaff_set.all()
        return DepartmentStaffModelSerializer(instance, many=True, context=self.context).data

    class Meta:
        model = Department
        fields = (
            'translations',
            'id',
            'head_image',
            'head_phone_number',
            'head_email',
            'head_instagram',
            'head_telegram',
            'head_facebook',

            # serializer fields
            'subject',
            'staff',
        )
