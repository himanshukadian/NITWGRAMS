# Generated by Django 2.2.5 on 2019-10-10 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comportal', '0023_auto_20191009_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='category',
            field=models.CharField(choices=[('E', 'electrical'), ('P', 'plumber'), ('C', 'carpenter'), ('H', 'housekeeping'), ('D', 'healthcare'), ('M', 'Mess')], default='H', max_length=1),
        ),
    ]
