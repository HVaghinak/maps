# Generated by Django 2.0.7 on 2018-07-27 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20180727_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='address_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
