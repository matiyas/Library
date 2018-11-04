from django.db import models
from django.core.validators import (
    MinValueValidator, MaxValueValidator, EmailValidator,
    MaxLengthValidator)
from django.utils import timezone
from BookBorrow.validators import author_birth_date_validator, reader_birth_date_validator


class AbstractCountry(models.Model):
    code = models.CharField(max_length=10, primary_key=True, )
    english_name = models.CharField(max_length=200)
    polish_name = models.CharField(max_length=200)

    def __str__(self):
        return self.english_name

    class Meta:
        abstract = True


class AbstractChoice(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Country(AbstractCountry):
    pass


class Language(AbstractCountry):
    pass


class Person(models.Model):
    first_name = models.CharField(max_length=200, validators=(MaxLengthValidator(200), ))
    last_name = models.CharField(max_length=200, validators=(MaxLengthValidator(200), ))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        abstract = True


class Author(Person):
    pass


class Publishment(AbstractChoice):
    pass


class Subject(AbstractChoice):
    pass


class Reader(Person):
    birth_date = models.DateField(validators=[reader_birth_date_validator, ])
    login = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=200, validators=(EmailValidator, ), unique=True)
    phone = models.CharField(max_length=20, unique=True)
    account_lock = models.BooleanField(default=False)
    penalty = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    books_limit = models.SmallIntegerField(default=2)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, to_field='code')
    city = models.CharField(max_length=200)
    post_code = models.CharField(max_length=20)
    street = models.CharField(max_length=200)
    apartment_nr = models.SmallIntegerField(blank=True, null=True)
    building_nr = models.SmallIntegerField()

    def __str__(self):
        return '[{}] {}'.format(self.login, super().__str__())


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    lang = models.ForeignKey(
        Language,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        to_field='code'
    )
    publishment = models.ForeignKey(
        Publishment,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    publication_year = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(timezone.datetime.now().year)
        ]
    )
    status = models.CharField(
        max_length=10,
        choices=(('0', 'Available'), ('1', 'Borrowed'), ('2', 'Reserved')),
        default='0',
        blank=True
    )
    return_date = models.DateTimeField(blank=True, null=True)
    queue = models.ManyToManyField(
        Reader, 
        through='BookQueue',
        through_fields=('book', 'reader'),
    )    

    def __str__(self):
        if self.author is not None:
            return '{}. {}, {}'.format(self.author.first_name[0], self.author.last_name, self.title)
        else:
            return self.title


class BookQueue(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)
