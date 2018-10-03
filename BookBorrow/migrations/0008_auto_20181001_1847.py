# Generated by Django 2.0.5 on 2018-10-01 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookBorrow', '0007_remove_publishment_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='reader',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='reader',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='BookBorrow.Country'),
        ),
        migrations.AddField(
            model_name='reader',
            name='first_name',
            field=models.CharField(default='FirstName', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reader',
            name='last_name',
            field=models.CharField(default='LastName', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reader',
            name='login',
            field=models.CharField(default='Login', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reader',
            name='password',
            field=models.CharField(default='password', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
    ]