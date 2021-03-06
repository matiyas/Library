# Generated by Django 2.1.2 on 2018-11-02 21:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookBorrow', '0006_auto_20181014_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=200, validators=[django.core.validators.MaxLengthValidator(200)]),
        ),
        migrations.AlterField(
            model_name='reader',
            name='last_name',
            field=models.CharField(max_length=200, validators=[django.core.validators.MaxLengthValidator(200)]),
        ),
    ]
