# Generated by Django 3.2.9 on 2024-04-30 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0010_alter_patientsinfo_patientimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientsinfo',
            name='patientImage',
            field=models.ImageField(upload_to='static/patientsUploadedImage'),
        ),
    ]
