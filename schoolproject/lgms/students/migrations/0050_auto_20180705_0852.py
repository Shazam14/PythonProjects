# Generated by Django 2.0.6 on 2018-07-05 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0049_auto_20180703_1111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentbio',
            options={'ordering': ['gradeyear']},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('CA', 'CASA Program'), ('SPED', 'Special Education Program'), ('SH', 'Senior High School Program'), ('GS', 'Grade School Program'), ('JH', 'Junior High School Program')], default='CA', help_text='Choose Application Program', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('C', 'Catholic'), ('B', 'Buddhist'), ('I', 'INC'), ('M', 'Muslim')], default='C', help_text='Please select your Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='studentbio',
            name='charactersets',
            field=models.ManyToManyField(to='students.CharacterBuildingActivities', verbose_name='Character Sets'),
        ),
        migrations.AlterField(
            model_name='studentbio',
            name='gradeyear',
            field=models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, related_name='gradeyear_gradeyear', to='students.GradeYear', verbose_name='Grade Year'),
        ),
        migrations.AlterField(
            model_name='studentbio',
            name='subjects',
            field=models.ManyToManyField(to='students.Subjects', verbose_name='List of Subjects'),
        ),
        migrations.RemoveField(
            model_name='studentbio',
            name='teachersname',
        ),
        migrations.AddField(
            model_name='studentbio',
            name='teachersname',
            field=models.ManyToManyField(to='students.Teachers', verbose_name='Teachers Name'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('CM', 'CASA AM'), ('G5', 'GRADE 5'), ('CA', 'CASA AFTERNOON 1:30'), ('G9', 'GRADE 9'), ('TEP-GR1', 'TEACH PM GRADE 1'), ('TEP-GR2', 'TEACH PM GRADE 3'), ('PG', 'PLAY GROUP'), ('G7', 'GRADE 7'), ('G3', 'GRADE 3'), ('TEP-GR2', 'TEACH PM GRADE 2'), ('G6', 'GRADE 6'), ('G8', 'GRADE 8'), ('TEP', 'TEACH PM'), ('G10', 'GRADE 10'), ('G1', 'GRADE 1'), ('G4', 'GRADE 4'), ('TEA', 'TEACH AM'), ('G2', 'GRADE 2')], default='CM', help_text='Choose Group for Students', max_length=10),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('S', 'STAFF'), ('SH', 'SCHOOL HEAD'), ('F', 'FACULTY')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
    ]