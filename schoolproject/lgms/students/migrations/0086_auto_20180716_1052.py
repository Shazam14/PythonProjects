# Generated by Django 2.0.6 on 2018-07-16 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0085_auto_20180716_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('GS', 'Grade School Program'), ('CA', 'CASA Program'), ('JH', 'Junior High School Program'), ('SPED', 'Special Education Program'), ('SH', 'Senior High School Program')], default='CA', help_text='Choose Application Program', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('W', 'Widowed'), ('SP', 'Single Parent'), ('M', 'Married'), ('D', 'Divorcee')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('B', 'Buddhist'), ('C', 'Catholic'), ('M', 'Muslim'), ('I', 'INC')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('LP', 'Lung Problem'), ('DP', 'Dermatology Problem'), ('HMP', 'Hematologic Problem'), ('TP', 'Thyroid Problem'), ('DM', 'Diabetes Mellitus'), ('CV', 'Convulsion'), ('HT', 'Hypertension'), ('MP', 'Metabolc Problem'), ('O', 'Others'), ('AST', 'Asthma'), ('VP', 'Viral Infection'), ('EPL', 'Epilepsy'), ('SZ', 'Seizures'), ('EP', 'Ear Problems'), ('GP', 'Gastrointestinal Problems'), ('HP', 'Heart Problem'), ('A', 'Allergy'), ('ANE', 'Anemia')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('0', 'OTHERS'), ('CO', 'COUGH'), ('H', 'HEADACHE'), ('L', 'LBM'), ('C', 'COLDS'), ('V', 'VOMITING'), ('D', 'DIARRHEA'), ('F', 'FEVER'), ('S', 'STOMACH ACHE')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='studentbio',
            name='username',
            field=models.OneToOneField(blank=True, max_length=64, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Primary User Info'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('G7', 'GRADE 7'), ('TEP-GR1', 'TEACH PM GRADE 1'), ('G2', 'GRADE 2'), ('G5', 'GRADE 5'), ('G10', 'GRADE 10'), ('TEP', 'TEACH PM'), ('G1', 'GRADE 1'), ('G6', 'GRADE 6'), ('G4', 'GRADE 4'), ('TEP-GR2', 'TEACH PM GRADE 3'), ('CA', 'CASA AFTERNOON 1:30'), ('G3', 'GRADE 3'), ('PG', 'PLAY GROUP'), ('CM', 'CASA AM'), ('G9', 'GRADE 9'), ('TEP-GR2', 'TEACH PM GRADE 2'), ('TEA', 'TEACH AM'), ('G8', 'GRADE 8')], default='CM', help_text='Choose Group for Students', max_length=10),
        ),
    ]