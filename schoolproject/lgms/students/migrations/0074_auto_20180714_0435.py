# Generated by Django 2.0.6 on 2018-07-14 04:35

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0073_auto_20180714_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='homenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='landline : +6328888888', max_length=128, verbose_name='Landline Number'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('SPED', 'Special Education Program'), ('CA', 'CASA Program'), ('JH', 'Junior High School Program'), ('SH', 'Senior High School Program'), ('GS', 'Grade School Program')], default='CA', help_text='Choose Application Program', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('D', 'Divorcee'), ('W', 'Widowed'), ('SP', 'Single Parent'), ('M', 'Married')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mobilenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='MOBILE FORMAT : +639178888888', max_length=128, verbose_name='Mobile Number'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('B', 'Buddhist'), ('M', 'Muslim'), ('I', 'INC'), ('C', 'Catholic')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('AST', 'Asthma'), ('EP', 'Ear Problems'), ('EPL', 'Epilepsy'), ('GP', 'Gastrointestinal Problems'), ('TP', 'Thyroid Problem'), ('MP', 'Metabolc Problem'), ('DP', 'Dermatology Problem'), ('ANE', 'Anemia'), ('LP', 'Lung Problem'), ('HMP', 'Hematologic Problem'), ('HT', 'Hypertension'), ('SZ', 'Seizures'), ('A', 'Allergy'), ('DM', 'Diabetes Mellitus'), ('CV', 'Convulsion'), ('HP', 'Heart Problem'), ('O', 'Others'), ('VP', 'Viral Infection')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('C', 'COLDS'), ('D', 'DIARRHEA'), ('F', 'FEVER'), ('CO', 'COUGH'), ('S', 'STOMACH ACHE'), ('L', 'LBM'), ('H', 'HEADACHE'), ('0', 'OTHERS'), ('V', 'VOMITING')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('CM', 'CASA AM'), ('CA', 'CASA AFTERNOON 1:30'), ('G4', 'GRADE 4'), ('G2', 'GRADE 2'), ('TEP-GR2', 'TEACH PM GRADE 2'), ('TEP-GR1', 'TEACH PM GRADE 1'), ('TEP-GR2', 'TEACH PM GRADE 3'), ('G6', 'GRADE 6'), ('PG', 'PLAY GROUP'), ('G8', 'GRADE 8'), ('G3', 'GRADE 3'), ('TEP', 'TEACH PM'), ('TEA', 'TEACH AM'), ('G7', 'GRADE 7'), ('G9', 'GRADE 9'), ('G10', 'GRADE 10'), ('G5', 'GRADE 5'), ('G1', 'GRADE 1')], default='CM', help_text='Choose Group for Students', max_length=10),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('SH', 'SCHOOL HEAD'), ('F', 'FACULTY'), ('S', 'STAFF')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
    ]