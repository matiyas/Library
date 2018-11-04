# Generated by Django 2.1.2 on 2018-10-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookBorrow', '0002_auto_20181014_1501'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[(0, 'Available'), (1, 'Borrowed'), (2, 'Reserved')], max_length=10),
        ),
    ]
