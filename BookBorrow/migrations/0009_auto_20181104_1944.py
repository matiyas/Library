# Generated by Django 2.1.2 on 2018-11-04 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookBorrow', '0008_auto_20181104_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='author',
            name='country',
        ),
        migrations.RemoveField(
            model_name='author',
            name='death_date',
        ),
    ]