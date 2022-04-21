# Generated by Django 3.2 on 2022-04-21 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['rank'], 'verbose_name': 'kafedra', 'verbose_name_plural': 'kafedralar'},
        ),
        migrations.AlterModelOptions(
            name='departmentstaff',
            options={'verbose_name': "kafedra o'qituvchisi", 'verbose_name_plural': "kafedra o'qituvchilari"},
        ),
        migrations.AlterModelOptions(
            name='departmentstafftranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': "kafedra o'qituvchisi Translation"},
        ),
        migrations.AlterModelOptions(
            name='departmentsubject',
            options={'verbose_name': 'kafedra fani', 'verbose_name_plural': 'kafedra fanlari'},
        ),
        migrations.AlterModelOptions(
            name='departmentsubjecttranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'kafedra fani Translation'},
        ),
        migrations.AlterModelOptions(
            name='departmenttranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'kafedra Translation'},
        ),
        migrations.AlterModelOptions(
            name='faculty',
            options={'ordering': ['rank'], 'verbose_name': 'fakultet', 'verbose_name_plural': 'fakultetlar'},
        ),
        migrations.AlterModelOptions(
            name='facultyadministration',
            options={'ordering': ['rank'], 'verbose_name': "fakultet ma'muriyati", 'verbose_name_plural': "fakultet ma'muriyatlari"},
        ),
        migrations.AlterModelOptions(
            name='facultyadministrationtranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': "fakultet ma'muriyati Translation"},
        ),
        migrations.AlterModelOptions(
            name='facultybachelor',
            options={'verbose_name': 'bakalavr', 'verbose_name_plural': 'bakalavrlar'},
        ),
        migrations.AlterModelOptions(
            name='facultybachelortranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'bakalavr Translation'},
        ),
        migrations.AlterModelOptions(
            name='facultymaster',
            options={'verbose_name': 'magistratura', 'verbose_name_plural': 'magistraturalar'},
        ),
        migrations.AlterModelOptions(
            name='facultymastertranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'magistratura Translation'},
        ),
        migrations.AlterModelOptions(
            name='facultytranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'fakultet Translation'},
        ),
        migrations.AlterModelOptions(
            name='rectorate',
            options={'ordering': ['rank'], 'verbose_name': 'rekrotat', 'verbose_name_plural': 'rekrotatlar'},
        ),
        migrations.AlterModelOptions(
            name='rectoratetranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'rekrotat Translation'},
        ),
        migrations.AlterField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.faculty', verbose_name='fakultet'),
        ),
        migrations.AlterField(
            model_name='department',
            name='head_email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='kafedra mudirining emaili'),
        ),
        migrations.AlterField(
            model_name='department',
            name='head_facebook',
            field=models.URLField(blank=True, verbose_name='kafedra mudirining facebooki'),
        ),
        migrations.AlterField(
            model_name='department',
            name='head_image',
            field=models.ImageField(upload_to='department_head/', verbose_name='kafedra mudirining rasmi'),
        ),
        migrations.AlterField(
            model_name='department',
            name='head_instagram',
            field=models.URLField(blank=True, verbose_name='kafedra mudirining instagrami'),
        ),
        migrations.AlterField(
            model_name='department',
            name='head_phone_number',
            field=models.CharField(max_length=17, verbose_name='kafedra mudirining telefon raqami'),
        ),
        migrations.AlterField(
            model_name='department',
            name='head_telegram',
            field=models.URLField(blank=True, verbose_name='kafedra mudirining telegrami'),
        ),
        migrations.AlterField(
            model_name='department',
            name='rank',
            field=models.PositiveSmallIntegerField(verbose_name="ketma-ketlikda chiqish o'rni"),
        ),
        migrations.AlterField(
            model_name='departmentstaff',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.department', verbose_name='kafedra'),
        ),
        migrations.AlterField(
            model_name='departmentstafftranslation',
            name='name',
            field=models.CharField(max_length=300, verbose_name="o'qituvchining to'liq ism-familyasi"),
        ),
        migrations.AlterField(
            model_name='departmentsubject',
            name='degree',
            field=models.CharField(choices=[('bachelor', 'Bakalavr'), ('master', 'Magistratura')], max_length=15, verbose_name='Qaysi darajaga tegishli'),
        ),
        migrations.AlterField(
            model_name='departmentsubject',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.department', verbose_name='kafedra'),
        ),
        migrations.AlterField(
            model_name='departmentsubjecttranslation',
            name='name',
            field=models.CharField(max_length=300, verbose_name='fan nomi'),
        ),
        migrations.AlterField(
            model_name='departmenttranslation',
            name='head_bio',
            field=models.TextField(blank=True, verbose_name='kafedra mudirining autobiografiyasi'),
        ),
        migrations.AlterField(
            model_name='departmenttranslation',
            name='head_full_name',
            field=models.CharField(max_length=300, verbose_name='kafedra mudirining ism-familyasi'),
        ),
        migrations.AlterField(
            model_name='departmenttranslation',
            name='history',
            field=models.TextField(help_text='HTML </code>', verbose_name='kafedra tarixi'),
        ),
        migrations.AlterField(
            model_name='departmenttranslation',
            name='name',
            field=models.CharField(max_length=300, verbose_name='nomi'),
        ),
        migrations.AlterField(
            model_name='departmenttranslation',
            name='other',
            field=models.TextField(help_text='HTML </code>', verbose_name="kafedra haqida qo'shimcha"),
        ),
        migrations.AlterField(
            model_name='departmenttranslation',
            name='reception_time',
            field=models.CharField(max_length=300, verbose_name='qabul vaqti'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='image',
            field=models.ImageField(upload_to='faculty/', verbose_name='rasmi'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='rank',
            field=models.PositiveSmallIntegerField(verbose_name="ketma-ketlikda chiqish o'rni"),
        ),
        migrations.AlterField(
            model_name='facultyadministration',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.faculty', verbose_name='fakultet'),
        ),
        migrations.AlterField(
            model_name='facultyadministration',
            name='image',
            field=models.ImageField(upload_to='faculty_administration/', verbose_name='rasmi'),
        ),
        migrations.AlterField(
            model_name='facultyadministration',
            name='phone_number',
            field=models.CharField(max_length=17, verbose_name='telefon raqami'),
        ),
        migrations.AlterField(
            model_name='facultyadministration',
            name='rank',
            field=models.PositiveSmallIntegerField(verbose_name="ketma-ketlikda chiqish o'rni"),
        ),
        migrations.AlterField(
            model_name='facultyadministrationtranslation',
            name='bio',
            field=models.TextField(blank=True, verbose_name='autobiografiyasi'),
        ),
        migrations.AlterField(
            model_name='facultyadministrationtranslation',
            name='full_name',
            field=models.CharField(max_length=300, verbose_name="to'liq ism-familyasi"),
        ),
        migrations.AlterField(
            model_name='facultyadministrationtranslation',
            name='position',
            field=models.CharField(max_length=300, verbose_name='lavozimi'),
        ),
        migrations.AlterField(
            model_name='facultyadministrationtranslation',
            name='reception_time',
            field=models.CharField(max_length=300, verbose_name='qabul vaqti'),
        ),
        migrations.AlterField(
            model_name='facultybachelor',
            name='code',
            field=models.CharField(max_length=20, verbose_name='kodi'),
        ),
        migrations.AlterField(
            model_name='facultybachelor',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.faculty', verbose_name='fakultet'),
        ),
        migrations.AlterField(
            model_name='facultybachelortranslation',
            name='name',
            field=models.CharField(max_length=300, verbose_name='nomi'),
        ),
        migrations.AlterField(
            model_name='facultymaster',
            name='code',
            field=models.CharField(max_length=20, verbose_name='kodi'),
        ),
        migrations.AlterField(
            model_name='facultymaster',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.faculty', verbose_name='fakultet'),
        ),
        migrations.AlterField(
            model_name='facultymastertranslation',
            name='name',
            field=models.CharField(max_length=300, verbose_name='nomi'),
        ),
        migrations.AlterField(
            model_name='facultytranslation',
            name='content',
            field=models.TextField(verbose_name="qisqacha ma'lumot"),
        ),
        migrations.AlterField(
            model_name='facultytranslation',
            name='name',
            field=models.CharField(max_length=300, verbose_name='nomi'),
        ),
        migrations.AlterField(
            model_name='rectorate',
            name='image',
            field=models.ImageField(upload_to='rectorate/', verbose_name='rasmi'),
        ),
        migrations.AlterField(
            model_name='rectorate',
            name='phone_number',
            field=models.CharField(max_length=17, verbose_name='telefon raqami'),
        ),
        migrations.AlterField(
            model_name='rectorate',
            name='rank',
            field=models.PositiveSmallIntegerField(verbose_name="ketma-ketlikda chiqish o'rni"),
        ),
        migrations.AlterField(
            model_name='rectoratetranslation',
            name='bio',
            field=models.TextField(blank=True, verbose_name='autobiografiyasi'),
        ),
        migrations.AlterField(
            model_name='rectoratetranslation',
            name='full_name',
            field=models.CharField(max_length=300, verbose_name="to'liq ism-familyasi"),
        ),
        migrations.AlterField(
            model_name='rectoratetranslation',
            name='position',
            field=models.CharField(max_length=300, verbose_name='lavozimi'),
        ),
        migrations.AlterField(
            model_name='rectoratetranslation',
            name='reception_time',
            field=models.CharField(max_length=300, verbose_name='qabul vaqti'),
        ),
    ]
