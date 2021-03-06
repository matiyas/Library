# Generated by Django 2.1.2 on 2018-10-14 12:24

import BookBorrow.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('birth_date', models.DateField(blank=True, null=True, validators=[BookBorrow.validators.BirthDateValidator('Author', 14)])),
                ('death_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('isbn', models.CharField(blank=True, max_length=13, null=True)),
                ('publication_year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2018)])),
                ('status', models.CharField(default=0, max_length=200)),
                ('return_time', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='BookBorrow.Author')),
            ],
        ),
        migrations.CreateModel(
            name='BookQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookBorrow.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('english_name', models.CharField(max_length=200)),
                ('polish_name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('english_name', models.CharField(max_length=200)),
                ('polish_name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Publishment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('birth_date', models.DateField(validators=[BookBorrow.validators.BirthDateValidator('Reader', 6)])),
                ('login', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200, validators=[django.core.validators.EmailValidator])),
                ('phone', models.CharField(max_length=20)),
                ('account_lock', models.BooleanField(default=False)),
                ('penalty', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('books_limit', models.SmallIntegerField(default=2)),
                ('city', models.CharField(max_length=200)),
                ('post_code', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=200)),
                ('apartment_nr', models.SmallIntegerField(blank=True, null=True)),
                ('building_nr', models.SmallIntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='BookBorrow.Country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='bookqueue',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookBorrow.Reader'),
        ),
        migrations.AddField(
            model_name='book',
            name='lang',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='BookBorrow.Language'),
        ),
        migrations.AddField(
            model_name='book',
            name='publishment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='BookBorrow.Publishment'),
        ),
        migrations.AddField(
            model_name='book',
            name='queue',
            field=models.ManyToManyField(through='BookBorrow.BookQueue', to='BookBorrow.Reader'),
        ),
        migrations.AddField(
            model_name='author',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='BookBorrow.Country'),
        ),
    ]
