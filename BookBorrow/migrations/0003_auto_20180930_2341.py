# Generated by Django 2.0.5 on 2018-09-30 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookBorrow', '0002_auto_20180930_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='id',
        ),
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(max_length=2, primary_key=True, serialize=False),
        ),
    ]