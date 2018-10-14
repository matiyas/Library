from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone
from .models import Author, Country


class AdminSiteTest(TestCase):
    def test_author_is_less_than_14_years_old(self):
        country = Country.objects.create(code='PL', english_name='Poland', polish_name='Polska')
        author = Author(
            first_name='Name',
            last_name='LastName',
            birth_date=timezone.now() - timezone.timedelta(days=365*14-1),
            country=country,
            death_date=timezone.now()
        )

        self.assertRaises(ValidationError, author.clean_fields)
