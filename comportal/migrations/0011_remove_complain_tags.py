# Generated by Django 2.2.5 on 2019-09-28 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comportal', '0010_auto_20190928_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complain',
            name='tags',
        ),
    ]
