# Generated by Django 2.1.2 on 2018-10-14 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookBorrow', '0004_auto_20181014_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='return_time',
            new_name='return_date',
        ),
    ]