# Generated by Django 2.0.6 on 2018-07-02 02:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0033_auto_20180702_0213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Teachers Info',
            },
        ),
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('SH', 'Senior High School Program'), ('CA', 'CASA Program'), ('SPED', 'Special Education Program'), ('GS', 'Grade School Program'), ('JH', 'Junior High School Program')], default='CA', help_text='Choose Application Program', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('M', 'Married'), ('SP', 'Single Parent'), ('W', 'Widowed'), ('D', 'Divorcee')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('I', 'INC'), ('B', 'Buddhist'), ('M', 'Muslim'), ('C', 'Catholic')], default='C', help_text='Please select your Religion', max_length=30),
        ),
        migrations.AddField(
            model_name='teachers',
            name='teachersname',
            field=models.ForeignKey(max_length=64, on_delete=django.db.models.deletion.CASCADE, related_name='teachers_name', to=settings.AUTH_USER_MODEL),
        ),
    ]