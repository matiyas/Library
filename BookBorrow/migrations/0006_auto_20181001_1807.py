# Generated by Django 2.0.5 on 2018-10-01 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookBorrow', '0005_auto_20181001_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=13, null=True),
        ),
    ]