from django.db import models

from parler.models import TranslatableModel, TranslatedFields


class Rectorate(TranslatableModel):
    translations = TranslatedFields(
        position=models.CharField(max_length=300, verbose_name="lavozimi"),
        full_name=models.CharField(max_length=300, verbose_name="to'liq ism-familyasi"),
        reception_time=models.CharField(max_length=300, verbose_name="qabul vaqti"),
        bio=models.TextField(blank=True, verbose_name="autobiografiyasi")
    )
    image = models.ImageField(upload_to='rectorate/', verbose_name='rasmi')
    phone_number = models.CharField(max_length=17, verbose_name="telefon raqami")

    email = models.EmailField(blank=True)
    instagram = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    rank = models.PositiveSmallIntegerField(verbose_name="ketma-ketlikda chiqish o'rni")

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['rank']
        verbose_name = "rekrotat"
        verbose_name_plural = "rekrotatlar"


class Faculty(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=300, verbose_name="nomi"),
        content=models.TextField(verbose_name="qisqacha ma'lumot")
    )
    image = models.ImageField(upload_to='faculty/', verbose_name="rasmi")

    rank = models.PositiveSmallIntegerField(verbose_name="ketma-ketlikda chiqish o'rni")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['rank']
        verbose_name = "fakultet"
        verbose_name_plural = "fakultetlar"


class FacultyAdministration(TranslatableModel):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, verbose_name="fakultet")
    translations = TranslatedFields(
        position=models.CharField(max_length=300, verbose_name="lavozimi"),
        full_name=models.CharField(max_length=300, verbose_name="to'liq ism-familyasi"),
        reception_time=models.CharField(max_length=300, verbose_name="qabul vaqti"),
        bio=models.TextField(blank=True, verbose_name="autobiografiyasi")
    )
    image = models.ImageField(upload_to='faculty_administration/', verbose_name="rasmi")
    phone_number = models.CharField(max_length=17, verbose_name="telefon raqami")

    email = models.EmailField(blank=True)
    instagram = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    rank = models.PositiveSmallIntegerField(verbose_name="ketma-ketlikda chiqish o'rni")

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['rank']
        verbose_name = "fakultet ma'muriyati"
        verbose_name_plural = "fakultet ma'muriyatlari"


class FacultyBachelor(TranslatableModel):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, verbose_name="fakultet")
    translations = TranslatedFields(
        name=models.CharField(max_length=300, verbose_name="nomi"),
    )
    code = models.CharField(max_length=20, verbose_name="kodi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "bakalavr"
        verbose_name_plural = "bakalavrlar"


class FacultyMaster(TranslatableModel):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, verbose_name="fakultet")
    translations = TranslatedFields(
        name=models.CharField(max_length=300, verbose_name="nomi"),
    )
    code = models.CharField(max_length=20, verbose_name="kodi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "magistratura"
        verbose_name_plural = "magistraturalar"


class Department(TranslatableModel):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, verbose_name="fakultet")
    translations = TranslatedFields(
        name=models.CharField(max_length=300, verbose_name="nomi"),
        head_full_name=models.CharField(max_length=300, verbose_name="kafedra mudirining ism-familyasi"),
        head_bio=models.TextField(blank=True, verbose_name="kafedra mudirining autobiografiyasi"),
        reception_time=models.CharField(max_length=300, verbose_name="qabul vaqti"),
        history=models.TextField(verbose_name="kafedra tarixi", help_text="HTML </code>"),  # ckeditor
        other=models.TextField(verbose_name="kafedra haqida qo'shimcha", help_text="HTML </code>"),  # ckeditor
    )
    head_image = models.ImageField(upload_to='department_head/', verbose_name="kafedra mudirining rasmi")
    head_phone_number = models.CharField(max_length=17, verbose_name="kafedra mudirining telefon raqami")

    head_email = models.EmailField(blank=True, verbose_name="kafedra mudirining emaili")
    head_instagram = models.URLField(blank=True, verbose_name="kafedra mudirining instagrami")
    head_telegram = models.URLField(blank=True, verbose_name="kafedra mudirining telegrami")
    head_facebook = models.URLField(blank=True, verbose_name="kafedra mudirining facebooki")

    rank = models.PositiveSmallIntegerField(verbose_name="ketma-ketlikda chiqish o'rni")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['rank']
        verbose_name = "kafedra"
        verbose_name_plural = "kafedralar"


class DepartmentSubject(TranslatableModel):
    DEGREE = (
        ('bachelor', 'Bakalavr'),
        ('master', 'Magistratura'),
    )
    department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name="kafedra")
    translations = TranslatedFields(
        name=models.CharField(max_length=300, verbose_name="fan nomi")
    )
    degree = models.CharField(max_length=15, choices=DEGREE, verbose_name="Qaysi darajaga tegishli")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "kafedra fani"
        verbose_name_plural = "kafedra fanlari"


class DepartmentStaff(TranslatableModel):
    department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name="kafedra")
    translations = TranslatedFields(
        name=models.CharField(max_length=300, verbose_name="o'qituvchining to'liq ism-familyasi")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "kafedra o'qituvchisi"
        verbose_name_plural = "kafedra o'qituvchilari"
