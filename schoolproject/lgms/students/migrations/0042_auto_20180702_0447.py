# Generated by Django 2.0.6 on 2018-07-02 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0041_auto_20180702_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('SH', 'Senior High School Program'), ('SPED', 'Special Education Program'), ('GS', 'Grade School Program'), ('JH', 'Junior High School Program'), ('CA', 'CASA Program')], default='CA', help_text='Choose Application Program', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('M', 'Married'), ('W', 'Widowed'), ('D', 'Divorcee'), ('SP', 'Single Parent')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('I', 'INC'), ('B', 'Buddhist'), ('C', 'Catholic'), ('M', 'Muslim')], default='C', help_text='Please select your Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='studentbio',
            name='studentname',
            field=models.ForeignKey(max_length=64, on_delete=django.db.models.deletion.CASCADE, related_name='customuser_childsname', to='students.Students'),
        ),
    ]
