# Generated by Django 2.1.4 on 2019-01-10 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comportal', '0004_auto_20181230_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='type',
            field=models.CharField(choices=[('G', 'green campus'), ('E', 'electrical'), ('C', 'civil')], default='G', max_length=1),
        ),
    ]