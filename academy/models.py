from django.db import models

from parler.models import TranslatableModel, TranslatedFields


class Faculty(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=300),
        content=models.TextField()
    )
    image = models.ImageField(upload_to='faculty/')

    rank = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['rank']


class FacultyAdministration(TranslatableModel):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)
    translations = TranslatedFields(
        position=models.CharField(max_length=300),
        full_name=models.CharField(max_length=300),
        reception_time=models.CharField(max_length=300),
        bio=models.TextField(blank=True)
    )
    image = models.ImageField(upload_to='faculty_administration/')
    phone_number = models.CharField(max_length=17)

    email = models.EmailField(blank=True)
    instagram = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    rank = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['rank']


class FacultyBachelor(TranslatableModel):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)
    translations = TranslatedFields(
        name=models.CharField(max_length=300),
    )
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class FacultyMaster(TranslatableModel):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)
    translations = TranslatedFields(
        name=models.CharField(max_length=300),
    )
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Department(TranslatableModel):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)
    translations = TranslatedFields(
        name=models.CharField(max_length=300),
        head_full_name=models.CharField(max_length=300),
        head_bio=models.TextField(blank=True),
        reception_time=models.CharField(max_length=300),
        history=models.TextField(),  # ckeditor
        other=models.TextField(),  # ckeditor at the last part
    )
    head_phone_number = models.CharField(max_length=17)

    head_email = models.EmailField(blank=True)
    head_instagram = models.URLField(blank=True)
    head_telegram = models.URLField(blank=True)
    head_facebook = models.URLField(blank=True)

    rank = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['rank']


class DepartmentSubject(TranslatableModel):
    DEGREE = (
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
    )
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    translations = TranslatedFields(
        name=models.CharField(max_length=300)
    )
    degree = models.CharField(max_length=15, choices=DEGREE)

    def __str__(self):
        return self.name


class DepartmentStaff(TranslatableModel):
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    translations = TranslatedFields(
        name=models.CharField(max_length=300)
    )

    def __str__(self):
        return self.name
