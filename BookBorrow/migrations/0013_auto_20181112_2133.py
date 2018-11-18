# Generated by Django 2.1.2 on 2018-11-12 20:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookBorrow', '0012_auto_20181104_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='reader',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='reader',
            name='last_name',
        ),
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default='Name', max_length=200, validators=[django.core.validators.MaxLengthValidator(200)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reader',
            name='name',
            field=models.CharField(default='Name', max_length=200, validators=[django.core.validators.MaxLengthValidator(200)]),
            preserve_default=False,
        ),
    ]