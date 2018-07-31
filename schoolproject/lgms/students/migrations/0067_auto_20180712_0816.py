# Generated by Django 2.0.6 on 2018-07-12 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0066_auto_20180712_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('JH', 'Junior High School Program'), ('SPED', 'Special Education Program'), ('CA', 'CASA Program'), ('GS', 'Grade School Program'), ('SH', 'Senior High School Program')], default='CA', help_text='Choose Application Program', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('W', 'Widowed'), ('D', 'Divorcee'), ('M', 'Married'), ('SP', 'Single Parent')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('M', 'Muslim'), ('C', 'Catholic'), ('B', 'Buddhist'), ('I', 'INC')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('MP', 'Metabolc Problem'), ('ANE', 'Anemia'), ('CV', 'Convulsion'), ('A', 'Allergy'), ('SZ', 'Seizures'), ('GP', 'Gastrointestinal Problems'), ('DP', 'Dermatology Problem'), ('EP', 'Ear Problems'), ('HMP', 'Hematologic Problem'), ('EPL', 'Epilepsy'), ('VP', 'Viral Infection'), ('AST', 'Asthma'), ('HT', 'Hypertension'), ('O', 'Others'), ('TP', 'Thyroid Problem'), ('LP', 'Lung Problem'), ('HP', 'Heart Problem'), ('DM', 'Diabetes Mellitus')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='observationlists',
            name='traitsname',
            field=models.CharField(max_length=300, verbose_name='Traits'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('D', 'DIARRHEA'), ('S', 'STOMACH ACHE'), ('0', 'OTHERS'), ('C', 'COLDS'), ('H', 'HEADACHE'), ('V', 'VOMITING'), ('CO', 'COUGH'), ('F', 'FEVER'), ('L', 'LBM')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('TEP-GR2', 'TEACH PM GRADE 2'), ('TEP', 'TEACH PM'), ('G2', 'GRADE 2'), ('CA', 'CASA AFTERNOON 1:30'), ('G7', 'GRADE 7'), ('G10', 'GRADE 10'), ('G5', 'GRADE 5'), ('PG', 'PLAY GROUP'), ('G1', 'GRADE 1'), ('G4', 'GRADE 4'), ('TEP-GR1', 'TEACH PM GRADE 1'), ('CM', 'CASA AM'), ('TEP-GR2', 'TEACH PM GRADE 3'), ('G3', 'GRADE 3'), ('G9', 'GRADE 9'), ('G8', 'GRADE 8'), ('TEA', 'TEACH AM'), ('G6', 'GRADE 6')], default='CM', help_text='Choose Group for Students', max_length=10),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('SH', 'SCHOOL HEAD'), ('F', 'FACULTY'), ('S', 'STAFF')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
    ]
