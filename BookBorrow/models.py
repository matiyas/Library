from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Country(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    english_name = models.CharField(max_length=200, null=True)
    polish_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.english_name


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        abstract = True


class Author(Person):
    death_date = models.DateField(null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, to_field='code')


class Publishment(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Address(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, to_field='code')
    city = models.CharField(max_length=200)
    post_code = models.CharField(max_length=20)
    street = models.CharField(max_length=200)
    apartment_nr = models.SmallIntegerField(null=True)
    building_nr = models.SmallIntegerField()

    def __str__(self):
        return '{}, {} {}'.format(self.city, self.street, self.apartment_nr)

    class Meta:
        verbose_name_plural = "Addresses"


class Reader(Person):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.OneToOneField(Address, on_delete=models.PROTECT)
    lock = models.BooleanField(default=False)
    penalty = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    books_limit = models.SmallIntegerField(default=2)

    def __str__(self):
        return '[' + self.login + '] ' + super().__str__()


class Status(models.Model):
    name = models.CharField(max_length=20)


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    lang = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, to_field='code')
    publishment = models.ForeignKey(Publishment, on_delete=models.SET_NULL, null=True)
    publication_year = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(timezone.datetime.now().year)
        ]
    )
    status = models.CharField(max_length=200, default=0)
    return_time = models.DateTimeField(null=True)
    queue = models.ManyToManyField(
        Reader, 
        through='BookQueue',
        through_fields=('book', 'reader'),
    )    

    def __str__(self):
        return self.author.first_name[0] + '. ' + self.author.last_name + ', ' + self.title


class BookQueue(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reservaton_date = models.DateTimeField(auto_now_add=True)
