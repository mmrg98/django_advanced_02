# Generated by Django 2.1.5 on 2020-09-13 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_auto_20200913_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='slug',
            field=models.SlugField(blank=True, default=None, unique=True),
        ),
    ]
