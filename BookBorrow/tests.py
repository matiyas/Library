import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Author, Country


class AuthorModelTest(TestCase):
    def test_new_author_with_birth_date_in_the_future(self):
        Country.objects.create(
            code='pl',
            english_name='Poland',
            polish_name='Polska'
        )

        Author.objects.create(
            first_name='Name',
            last_name='Surname',
            birth_date=timezone.now() + timezone.timedelta(days=1),
            country=Country.objects.get(code='pl')
        )

        self.assertIsNone(Author.objects.all())
