# Generated by Django 2.2.5 on 2019-10-05 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comportal', '0021_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Image'),
        ),
    ]
