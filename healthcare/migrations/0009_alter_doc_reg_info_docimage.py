# Generated by Django 3.2.9 on 2024-04-30 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0008_alter_doc_reg_info_docimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc_reg_info',
            name='docImage',
            field=models.ImageField(upload_to='static/doctorsUploadedImage'),
        ),
    ]
